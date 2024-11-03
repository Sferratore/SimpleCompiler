class Variable:
    def __init__(self, name):
        self.name = name  # Nome della variabile, ad esempio "x" o "y"

    def __repr__(self):
        return f"Variable(name={self.name})"