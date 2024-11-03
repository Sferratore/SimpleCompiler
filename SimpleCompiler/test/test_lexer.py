from Lexer import Lexer
import unittest


class TestLexer(unittest.TestCase):

    def test_tokenize_correct_code(self):
        # Arrange
        code = '''
        float x = 10;
        float y = 3.14;
        incase (x >= y) {
            during(3 > 2){}
        }
        '''
        l = Lexer()
        # Act
        tokens = l.tokenize(code)
        print(tokens)
        # Assert
        self.assertEqual(tokens.__str__(), "[('KEYWORD', 'float'), ('ID', 'x'), ('ASSIGN', '='), ('NUM', '10'), ('SEMI', ';'), ('KEYWORD', 'float'), ('ID', 'y'), ('ASSIGN', '='), ('NUM', '3.14'), ('SEMI', ';'), ('KEYWORD', 'incase'), ('LPAR', '('), ('ID', 'x'), ('RELOP', '>='), ('ID', 'y'), ('RPAR', ')'), ('LBRA', '{'), ('KEYWORD', 'during'), ('LPAR', '('), ('NUM', '3'), ('RELOP', '>'), ('NUM', '2'), ('RPAR', ')'), ('LBRA', '{'), ('RBRA', '}'), ('RBRA', '}')]")
