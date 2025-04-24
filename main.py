"""
Script principal para calcular y mostrar los conjuntos FIRST y FOLLOW
de una gramática dada.
"""

import argparse
import sys
import grammar as grammar_module

from first import compute_first
from follow import compute_follow
from utils import load_grammar_from_json, load_grammar_from_bnf

def parse_args():
    parser = argparse.ArgumentParser(
        description='Calcula FIRST y FOLLOW de una gramática (JSON o BNF).'
    )
    parser.add_argument(
        '--input', '-i',
        help='Ruta a archivo JSON o BNF que define la gramática',
        required=False
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # Carga gramática: si se pasó --input, detecta JSON o BNF; si no, usa la de default
    if args.input:
        path = args.input
        if path.endswith('.json'):
            grammar, start_symbol = load_grammar_from_json(path)
        else:
            grammar, start_symbol = load_grammar_from_bnf(path)
    else:
        # Aquí referimos al módulo, no a nombres sueltos
        grammar = grammar_module.grammar
        start_symbol = grammar_module.start_symbol

    # Calcula FIRST
    first_sets = compute_first(grammar)
    print("FIRST sets:")
    for nt, s in first_sets.items():
        print(f"  FIRST({nt}) = {{ {', '.join(sorted(s))} }}")

    # Calcula FOLLOW
    follow_sets = compute_follow(grammar, start_symbol, first_sets)
    print("\nFOLLOW sets:")
    for nt, s in follow_sets.items():
        print(f"  FOLLOW({nt}) = {{ {', '.join(sorted(s))} }}")


if __name__ == "__main__":
    main()
