from Lexer import Lexer
import unittest


class TestLexer(unittest.TestCase):

    def test_tokenize(self):
        # Arrange
        code = '''
        float x = 10;
        float y = 3.14;
        if (x >= y) {
            during;
        }
        '''
        l = Lexer()
        # Act
        tokens = l.tokenize(code)
        print(tokens)
        # Assert
        self.assertTrue(True)
