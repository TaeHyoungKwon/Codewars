import math
import unittest


def square_it(digits):
    if math.sqrt(len(str(digits))).is_integer():
        temp = []
        result = []
        for i, char in enumerate(str(digits), 1):
            if i % math.sqrt(len(str(digits))) == 0:
                temp.append(char)
                result.append(''.join(temp))
                temp = []
            else:
                temp.append(char)
        return '\n'.join(result)
    return "Not a perfect square!"


class TestSquareIt(unittest.TestCase):
    def test_square_it_should_return_not_a_perfect_square_message_when_given_digits_is_not_perfect_square_length(self):
        digits = 222
        actual = square_it(digits)
        self.assertEqual(actual, "Not a perfect square!")

    def test_square_it_should_return_a_perfect_square_message_when_given_digits_is_perfect_square_length(self):
        digits = 112141568
        actual = square_it(digits)
        self.assertEqual(actual, "112\n141\n568")
