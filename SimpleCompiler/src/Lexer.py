import re

# Token definition
token_specification = [
    ('NUM', r'\d+(\.\d+)?(E[+-]?\d+)?'),         # Numbers
    ('ID', r'[A-Za-z_][A-Za-z_0-9]*'),           # Identificators
    ('ASSIGN', r'='),                            # Assignment operator
    ('RELOP', r'<=|>=|==|<>|<|>'),               # Relational Operators
    ('LPAR', r'\('),                             # Opened par
    ('RPAR', r'\)'),                             # Closed par
    ('LBRA', r'\{'),                             # Open brackets
    ('RBRA', r'\}'),                             # Closed brackets
    ('SEMI', r';'),                              # Semicolon
    ('KEYWORD', r'\b(?:int|float|during|incase|otherwise)\b'), # Keywords
    ('DELIM', r'[ \n\t\r]+'),                    # Blank Spaces
]

# RegEx Compilation
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

# Lexer function
def lexer(code):
    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type == 'ID':
            print(f'Token({token_type}, {token_value}, PUNTATORE ALLA TABELLA SIMBOLI)')
        elif token_type == 'NUM':
            print(f'Token({token_type}, {token_value})')
        elif token_type == 'DELIM':
            continue
        else:
            print(f'Token({token_type}, {token_value})')



