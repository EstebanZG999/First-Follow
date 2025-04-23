"""
Script principal para calcular y mostrar los conjuntos FIRST y FOLLOW
de una gramática dada.
"""

from grammar import grammar, start_symbol
from first import compute_first
from follow import compute_follow


def main():
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
