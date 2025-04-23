def compute_first(grammar):
    first = { nt: set() for nt in grammar }  # FIRST sets vacíos
    changed = True

    while changed:
        changed = False
        for nt, prods in grammar.items():
            for prod in prods:
                # caso: producción vacía
                if prod == ["ε"]:
                    if "ε" not in first[nt]:
                        first[nt].add("ε")
                        changed = True
                    continue

                # recorremos símbolos de la derecha
                nullable_prefix = True
                for sym in prod:
                    if sym not in grammar:  # es terminal
                        if sym not in first[nt]:
                            first[nt].add(sym)
                            changed = True
                        nullable_prefix = False
                        break
                    else:
                        # añadimos FIRST(sym) \ {ε} a FIRST(nt)
                        before = len(first[nt])
                        first[nt] |= (first[sym] - {"ε"})
                        if len(first[nt]) > before:
                            changed = True
                        # si FIRST(sym) contiene ε, seguimos; si no, cortamos
                        if "ε" in first[sym]:
                            nullable_prefix = True
                        else:
                            nullable_prefix = False
                            break

                # si todos los símbolos pueden derivar ε, entonces ε ∈ FIRST(nt)
                if nullable_prefix:
                    if "ε" not in first[nt]:
                        first[nt].add("ε")
                        changed = True

    return first