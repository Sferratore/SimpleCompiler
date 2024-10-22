class Token:
    def __init__(self, token_type, value, symbol_table_pointer=None):
        """
        Initializes a new Token.

        :param token_type: The type of the token (e.g., 'ID', 'NUM', 'KEYWORD', etc.)
        :param value: The actual value of the token (e.g., 'x', '10', 'int', etc.)
        :param symbol_table_pointer: Optional pointer to the symbol table (for ID tokens).
        """
        self.token_type = token_type
        self.value = value
        self.symbol_table_pointer = symbol_table_pointer

    def __repr__(self):
        """
        Returns a string representation of the token
        """
        if self.symbol_table_pointer:
            return f"Token({self.token_type}, {self.value}, symbol_table_pointer={self.symbol_table_pointer})"
        else:
            return f"Token({self.token_type}, {self.value})"
