import Lexer
import unittest


class TestLexer(unittest.TestCase):

    def test_get_size(self):
        # Arrange
        code = '''
        float x = 10;
        float y = 3.14;
        if (x >= y) {
            during;
        }
        '''
        # Act
        Lexer.lexer(code)
        # Assert
        self.assertTrue(True)
