import Program
import Declaration
import Number
import Variable

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens  # Lista dei token dal lexer
        self.pos = 0          # Posizione corrente del token

    def _current_token(self):
        # Restituisce il token corrente
        return self.tokens[self.pos]

    def _advance(self):
        # Passa al token successivo
        if not self._is_at_end():
            self.pos += 1

    def _is_at_end(self):
        # Controlla se abbiamo raggiunto la fine dei token
        return self.pos >= len(self.tokens)

    def parse_program(self):
        # Punto di partenza per l'analisi del programma
        statements = []
        while not self._is_at_end():
            statements.append(self.parse_statement())
        return Program(statements)  # Nodo radice dell'AST

    def parse_statement(self):
        # Analizza una singola istruzione
        token = self._current_token()
        if token[0] == 'KEYWORD' and token[1] in ('int', 'float'):
            return self.parse_declaration()
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def parse_declaration(self):
        # Analizza una dichiarazione di variabile, es. "int x = 5;"
        var_type = self._current_token()[1]  # "int" o "float"
        self._advance()  # Avanza al nome della variabile

        if self._current_token()[0] == 'ID':  # Nome della variabile
            var_name = self._current_token()[1]
            self._advance()

            if self._current_token()[0] == 'ASSIGN':  # Operatore "="
                self._advance()
                expr = self.parse_expression()  # Valore da assegnare

                if self._current_token()[0] == 'SEMI':  # Fine istruzione con ";"
                    self._advance()
                    return Declaration(var_type, var_name, expr)
                else:
                    raise SyntaxError("Missing ';' at end of declaration.")
            else:
                raise SyntaxError("Expected '=' in declaration.")
        else:
            raise SyntaxError("Expected variable name.")

    def parse_expression(self):
        # Analizza un'espressione (qui gestiamo solo numeri per semplicità)
        token = self._current_token()
        if token[0] == 'NUM':
            self._advance()
            return Number(token[1])
        elif token[0] == 'ID':  # Variabile usata in un'espressione
            self._advance()
            return Variable(token[1])
        else:
            raise SyntaxError(f"Unexpected token in expression: {token}")
