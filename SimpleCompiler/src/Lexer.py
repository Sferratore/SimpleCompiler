import re

class Lexer:
    def __init__(self):
        # Token specification
        self.token_specification = [
            ('KEYWORD', r'\b(?:int|float|during|incase|otherwise)\b'),  # Keywords
            ('NUM', r'\d+(\.\d+)?(E[+-]?\d+)?'),                        # Numbers
            ('ID', r'[A-Za-z_][A-Za-z_0-9]*'),                          # Identificators
            ('ASSIGN', r'='),                                           # Assignment operator
            ('RELOP', r'<=|>=|==|<>|<|>'),                              # Relational Operators
            ('LPAR', r'\('),                                            # Open paren
            ('RPAR', r'\)'),                                            # Closed paren
            ('LBRA', r'\{'),                                            # Open bracket
            ('RBRA', r'\}'),                                            # Closed bracket
            ('SEMI', r';'),                                             # Semicolon
            ('DELIM', r'[ \n\t\r]+'),                                   # Blank Spaces
        ]
        # Compile regex for tokenization

        self.token_regex = self._compile_regex()

    def _compile_regex(self):
        """
        Compile the regular expressions for tokenizing the input code.
        """
        return '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specification)

    def tokenize(self, code):
        """
        Tokenize the given source code and return a list of tokens.
        """
        tokens = []
        for match in re.finditer(self.token_regex, code):
            token_type = match.lastgroup
            token_value = match.group(token_type)
            if token_type == 'DELIM':
                continue  # Ignore delimiters like spaces, tabs, and newlines
            tokens.append((token_type, token_value))
        return tokens

    def print_tokens(self, code):
        """
        Print the tokens identified in the input code.
        """
        for match in re.finditer(self.token_regex, code):
            token_type = match.lastgroup
            token_value = match.group(token_type)
            if token_type == 'ID':
                print(f'Token({token_type}, {token_value})')
            elif token_type == 'NUM':
                print(f'Token({token_type}, {token_value})')
            elif token_type == 'DELIM':
                continue
            else:
                print(f'Token({token_type}, {token_value})')