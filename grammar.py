"""
Definición de la gramática de ejemplo:
  E  → T E'
  E' → + T E' | ε
  T  → F T'
  T' → * F T' | ε
  F  → ( E ) | id
"""

# Diccionario: no terminal → lista de producciones
grammar = {
    "E":  [["T", "E'"]],
    "E'": [["+", "T", "E'"], ["ε"]],
    "T":  [["F", "T'"]],
    "T'": [["*", "F", "T'"], ["ε"]],
    "F":  [["(", "E", ")"], ["id"]],
}

# Símbolo inicial
start_symbol = "E"
