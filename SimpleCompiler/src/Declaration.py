class Declaration:
    def __init__(self, var_type, var_name, expression):
        self.var_type = var_type         # Tipo della variabile (es. "int", "float")
        self.var_name = var_name         # Nome della variabile (es. "x")
        self.expression = expression     # Espressione assegnata alla variabile (es. Number(5))

    def __repr__(self):
        return f"Declaration(var_type={self.var_type}, var_name={self.var_name}, expression={self.expression})"