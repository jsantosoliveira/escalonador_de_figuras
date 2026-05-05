# 📐 Escalonador de Figuras

> Aplicação de escala com análise de variação de área — Projeto Integrador de Álgebra Linear 2026/1  
> CIESA – Bacharelado em Ciência da Computação

---

## 👥 Integrantes

| Nome | Matrícula |
|---|---|
| Caio Rodolfo Rodrigues Maciel | — |
| Iago Albuquerque Rodrigues | — |
| Josias dos Santos Oliveira | — |
| Logan Gabriel Soares Castro | — |

**Professor:** Francisco de Assis Souza de Oliveira

---

## 📌 Sobre o Projeto

Este projeto demonstra a aplicação prática de **transformações lineares de escala** em ambientes bidimensionais (ℝ²), validando matematicamente a relação entre o **determinante da matriz de transformação** e o **fator de variação de área** da figura resultante.

Dado um polígono de entrada, o programa:

1. Constrói a **matriz de escala** `S = diag(sx, sy)`
2. Aplica a transformação `V' = S · V` sobre os vértices
3. Calcula as áreas usando a **Fórmula de Shoelace**
4. Valida que `A_t = |det(S)| · A_o`
5. Gera uma **visualização gráfica** comparativa

---

## 🧮 Fundamentação Matemática

A matriz de escala utilizada é:

```
S = | sx   0 |
    |  0  sy |
```

A variação de área é dada por:

```
A_transformada = |det(S)| × A_original
det(S) = sx × sy
```

A área dos polígonos é calculada pela **Fórmula de Shoelace**:

```
A = ½ |Σ (xᵢ · yᵢ₊₁ − xᵢ₊₁ · yᵢ)|
```

---

## 🗂️ Estrutura do Repositório

```
escalonador_de_figuras/
├── escalonador.py            # Código principal
├── requirements.txt          # Dependências
├── resultado_escalonamento.png  # Gerado após execução
├── relatorio/
│   └── relatorio_tecnico.pdf
└── README.md
```

---

## ⚙️ Pré-requisitos

- Python **3.10+**
- pip

---

## 🚀 Como Rodar

### 1. Clone o repositório

```bash
git clone https://github.com/<seu-usuario>/escalonador_de_figuras.git
cd escalonador_de_figuras
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute

```bash
python escalonador.py
```

### 5. Interaja com o programa

```
══════════════════════════════════════════════════
   ESCALONADOR DE FIGURAS — Álgebra Linear
══════════════════════════════════════════════════

  Digite o fator de escala horizontal (sx): 2.0
  Digite o fator de escala vertical   (sy): 1.5
```

---

## 📊 Exemplo de Saída

```
──────────────────────────────────────────────────
  RESULTADOS MATEMÁTICOS
──────────────────────────────────────────────────
  Área original          : 4.0000 u.a.
  Área transformada      : 12.0000 u.a.
  det(S) = sx · sy       : 3.0000
  Fator de variação real : 3.0000
  Fator esperado |det(S)|: 3.0000
──────────────────────────────────────────────────
  ✅ SUCESSO: A teoria foi validada!
     A_t = |det(S)| · A_o  →  12.00 = 3.00 × 4.00
──────────────────────────────────────────────────

  📊 Gráfico salvo como: resultado_escalonamento.png
```

O gráfico gerado mostra a figura **original em azul** e a figura **escalonada em verde**.

---

## 📦 Dependências

```
numpy
matplotlib
```

---

## 🧠 Complexidade

| Operação | Complexidade |
|---|---|
| Cálculo de área (Shoelace) | O(n) |
| Transformação linear (S · V) | O(n) |
| Espaço em memória | O(n) |

Onde `n` é o número de vértices do polígono.

---

## 📄 Licença

Projeto acadêmico — uso educacional.
