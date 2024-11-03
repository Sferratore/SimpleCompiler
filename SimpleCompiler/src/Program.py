class Program:
    def __init__(self, statements):
        self.statements = statements  # Lista di nodi AST per ogni istruzione

    def __repr__(self):
        return f"Program(statements={self.statements})"