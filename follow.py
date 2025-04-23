def compute_follow(grammar, start_symbol, first):
    follow = { nt: set() for nt in grammar }
    follow[start_symbol].add("$")   # marcador de fin de cadena

    changed = True
    while changed:
        changed = False
        for nt, prods in grammar.items():
            for prod in prods:
                trailer = follow[nt].copy()
                # recorremos la producción de derecha a izquierda
                for sym in reversed(prod):
                    if sym in grammar:  # si es no terminal
                        before = len(follow[sym])
                        follow[sym] |= trailer
                        if len(follow[sym]) > before:
                            changed = True

                        # si FIRST(sym) contiene ε, extendemos trailer
                        if "ε" in first[sym]:
                            trailer |= (first[sym] - {"ε"})
                        else:
                            trailer = first[sym] - {"ε"}
                    else:
                        # sym es terminal: el trailer pasa a ser {sym}
                        trailer = {sym}

    return follow
