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
        tokens = []
        pos = 0
        while pos < len(code):
            match = re.match(self.token_regex, code[pos:])
            if match:
                token_type = match.lastgroup
                token_value = match.group(token_type)
                if token_type != 'DELIM':  # Ignore delimiters like spaces, tabs, and newlines
                    tokens.append((token_type, token_value))
                pos += len(token_value)  # Move forward by the length of the matched token
            else:
                # Raise an error if no valid token is found at this position
                raise ValueError(f"Unknown token sequence at position {pos}: {code[pos:pos+10]}")
        return tokens