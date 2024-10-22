from Token import Token
import unittest


class TestToken(unittest.TestCase):

    def test_token_correct(self):
        # Arrange
        t = Token("INT", "6")
        # Act
        token_str = t.__str__()
        # Assert
        self.assertEqual(token_str, "Token(INT, 6)")
