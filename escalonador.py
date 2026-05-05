"""
Escalonador de Figuras
======================
Projeto Integrador – Álgebra Linear 2026/1
CIESA – Bacharelado em Ciência da Computação

Aplicação de escala com análise de variação de área usando
transformações lineares e a Fórmula de Shoelace.

Integrantes:
    - Caio Rodolfo Rodrigues Maciel
    - Iago Albuquerque Rodrigues
    - Josias dos Santos Oliveira
    - Logan Gabriel Soares Castro

Professor: Francisco de Assis Souza de Oliveira
"""

import numpy as np
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────
# 1. MÓDULO DE ENTRADA
# ──────────────────────────────────────────────

def obter_vertices() -> np.ndarray:
    """
    Define os vértices do polígono original.

    Retorna uma matriz 2×n onde cada coluna é um vetor posição [x, y].
    Padrão: quadrado de lado 2 com origem em (0, 0).
    """
    vertices = np.array([
        [0, 2, 2, 0],   # coordenadas x
        [0, 0, 2, 2]    # coordenadas y
    ], dtype=float)
    return vertices


def obter_fatores_escala() -> tuple[float, float]:
    """
    Solicita ao usuário os fatores de escala sx e sy.
    Aceita valores decimais positivos (ex: 2.0, 1.5).
    """
    print("\n" + "═" * 50)
    print("   ESCALONADOR DE FIGURAS — Álgebra Linear")
    print("═" * 50)

    while True:
        try:
            sx = float(input("\n  Digite o fator de escala horizontal (sx): "))
            sy = float(input("  Digite o fator de escala vertical   (sy): "))
            if sx <= 0 or sy <= 0:
                print("  ⚠  Os fatores devem ser positivos. Tente novamente.")
                continue
            return sx, sy
        except ValueError:
            print("  ⚠  Entrada inválida. Use números como 2 ou 1.5.")


# ──────────────────────────────────────────────
# 2. FUNÇÃO DE ÁREA — Fórmula de Shoelace
# ──────────────────────────────────────────────

def calcular_area(vertices: np.ndarray) -> float:
    """
    Calcula a área de um polígono usando a Fórmula de Shoelace (Teorema de Green discreto).

    Parâmetros:
        vertices (np.ndarray): matriz 2×n com coordenadas [x; y].

    Retorna:
        float: área do polígono em unidades de área (u.a.).

    Complexidade: O(n) — percorre os vértices uma única vez.
    """
    x = vertices[0]
    y = vertices[1]

    # Produto cruzado vetorizado usando np.roll para deslocar índices
    area = 0.5 * np.abs(
        np.dot(x, np.roll(y, -1)) - np.dot(np.roll(x, -1), y)
    )
    return area


# ──────────────────────────────────────────────
# 3. PROCESSAMENTO MATRICIAL
# ──────────────────────────────────────────────

def construir_matriz_escala(sx: float, sy: float) -> np.ndarray:
    """
    Constrói a matriz de escala S diagonal de ordem 2:

        S = | sx   0 |
            |  0  sy |

    Parâmetros:
        sx (float): fator de escala no eixo x.
        sy (float): fator de escala no eixo y.

    Retorna:
        np.ndarray: matriz 2×2 de transformação.
    """
    return np.array([
        [sx, 0],
        [0, sy]
    ], dtype=float)


def aplicar_transformacao(S: np.ndarray, V: np.ndarray) -> np.ndarray:
    """
    Aplica a transformação linear ao conjunto de vértices.

    Operação: V' = S · V

    Parâmetros:
        S (np.ndarray): matriz de escala 2×2.
        V (np.ndarray): matriz de vértices 2×n.

    Retorna:
        np.ndarray: novos vértices transformados V'.

    Complexidade: O(n) para matriz 2×2 × 2×n.
    """
    return np.dot(S, V)


# ──────────────────────────────────────────────
# 4. MÓDULO DE VALIDAÇÃO
# ──────────────────────────────────────────────

def validar_teoria(S: np.ndarray, area_original: float, area_transformada: float) -> None:
    """
    Valida a propriedade fundamental:

        A_t = |det(S)| · A_o

    onde det(S) = sx · sy para matrizes diagonais.

    Parâmetros:
        S (np.ndarray): matriz de transformação.
        area_original (float): área antes da transformação.
        area_transformada (float): área após a transformação.
    """
    determinante = np.linalg.det(S)
    fator_calculado = area_transformada / area_original
    fator_esperado = abs(determinante)

    print("\n" + "─" * 50)
    print("  RESULTADOS MATEMÁTICOS")
    print("─" * 50)
    print(f"  Área original          : {area_original:.4f} u.a.")
    print(f"  Área transformada      : {area_transformada:.4f} u.a.")
    print(f"  det(S) = sx · sy       : {determinante:.4f}")
    print(f"  Fator de variação real : {fator_calculado:.4f}")
    print(f"  Fator esperado |det(S)|: {fator_esperado:.4f}")
    print("─" * 50)

    # Arredondamento para evitar erros de ponto flutuante
    if round(fator_calculado, 10) == round(fator_esperado, 10):
        print("  ✅ SUCESSO: A teoria foi validada!")
        print(f"     A_t = |det(S)| · A_o  →  {area_transformada:.2f} = {fator_esperado:.2f} × {area_original:.2f}")
    else:
        print("  ❌ FALHA: Os valores não coincidem. Verifique os dados.")

    print("─" * 50 + "\n")


# ──────────────────────────────────────────────
# 5. MÓDULO DE VISUALIZAÇÃO
# ──────────────────────────────────────────────

def fechar_poligono(vertices: np.ndarray) -> np.ndarray:
    """Fecha o polígono repetindo o primeiro vértice no final."""
    return np.hstack([vertices, vertices[:, [0]]])


def plotar_figuras(V_original: np.ndarray, V_transformado: np.ndarray,
                   sx: float, sy: float) -> None:
    """
    Gera a visualização comparativa entre a figura original e a escalonada.

    Parâmetros:
        V_original (np.ndarray): vértices originais.
        V_transformado (np.ndarray): vértices após transformação.
        sx (float): fator horizontal aplicado.
        sy (float): fator vertical aplicado.
    """
    fig, ax = plt.subplots(figsize=(8, 7))
    fig.patch.set_facecolor("#F8F9FA")
    ax.set_facecolor("#F8F9FA")

    Vo = fechar_poligono(V_original)
    Vt = fechar_poligono(V_transformado)

    # Figura original
    ax.fill(Vo[0], Vo[1], alpha=0.3, color="#1565C0", label="Original")
    ax.plot(Vo[0], Vo[1], color="#1565C0", linewidth=2)

    # Figura transformada
    ax.fill(Vt[0], Vt[1], alpha=0.3, color="#2E7D32", label=f"Escalonada (sx={sx}, sy={sy})")
    ax.plot(Vt[0], Vt[1], color="#2E7D32", linewidth=2)

    # Marcação dos vértices
    ax.scatter(V_original[0], V_original[1], color="#1565C0", zorder=5, s=60)
    ax.scatter(V_transformado[0], V_transformado[1], color="#2E7D32", zorder=5, s=60)

    # Origem
    ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")
    ax.axvline(0, color="gray", linewidth=0.8, linestyle="--")
    ax.plot(0, 0, "ko", markersize=6, label="Origem (0,0)")

    ax.set_title(
        f"Escalonador de Figuras  |  S = diag({sx}, {sy})  |  det(S) = {sx * sy}",
        fontsize=13, fontweight="bold", pad=15
    )
    ax.set_xlabel("Eixo X", fontsize=11)
    ax.set_ylabel("Eixo Y", fontsize=11)
    ax.legend(fontsize=10, loc="upper left")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_aspect("equal")

    plt.tight_layout()
    plt.savefig("resultado_escalonamento.png", dpi=150, bbox_inches="tight")
    print("  📊 Gráfico salvo como: resultado_escalonamento.png")
    plt.show()


# ──────────────────────────────────────────────
# 6. PIPELINE PRINCIPAL
# ──────────────────────────────────────────────

def main() -> None:
    # Entrada
    sx, sy = obter_fatores_escala()

    # Vértices originais (quadrado 2×2)
    V = obter_vertices()

    # Matriz de escala
    S = construir_matriz_escala(sx, sy)

    # Transformação: V' = S · V
    V_linha = aplicar_transformacao(S, V)

    # Áreas
    area_original = calcular_area(V)
    area_transformada = calcular_area(V_linha)

    # Validação
    validar_teoria(S, area_original, area_transformada)

    # Visualização
    plotar_figuras(V, V_linha, sx, sy)


if __name__ == "__main__":
    main()

