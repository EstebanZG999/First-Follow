import json
import re

def load_grammar_from_json(path):
    """
    Carga una gramática desde un archivo JSON con la estructura:
    { "grammar": { ... }, "start_symbol": "..." }
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    grammar = data.get('grammar', {})
    start_symbol = data.get('start_symbol')
    if not grammar or not start_symbol:
        raise ValueError(f"JSON inválido: faltan 'grammar' o 'start_symbol' en {path}")
    return grammar, start_symbol


def load_grammar_from_bnf(path):
    """
    Carga una gramática en formato BNF simple, asumiendo líneas como:
        <A> ::= X Y | ε
    Devuelve (grammar_dict, start_symbol).
    """
    grammar = {}
    start_symbol = None
    pattern = re.compile(r"^<(?P<nt>[^>]+)>\s*::=\s*(?P<rhs>.+)")

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            m = pattern.match(line)
            if not m:
                continue
            nt = m.group('nt')
            if start_symbol is None:
                start_symbol = nt
            productions = [p.strip() for p in m.group('rhs').split('|')]

            grammar.setdefault(nt, [])
            for prod in productions:
                symbols = []
                for token in re.findall(r"<[^>]+>|ε|[^\s]+", prod):
                    if token.startswith('<') and token.endswith('>'):
                        symbols.append(token[1:-1])
                    else:
                        symbols.append(token)
                grammar[nt].append(symbols)

    if not grammar:
        raise ValueError(f"No se pudo parsear BNF en {path}")
    return grammar, start_symbol
