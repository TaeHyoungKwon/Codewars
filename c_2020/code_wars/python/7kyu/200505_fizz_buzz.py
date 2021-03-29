import unittest


def fizzbuzz(n):
    result = []
    for ele in range(1, n + 1):
        if ele % 15 == 0:
            result.append('FizzBuzz')
        elif ele % 3 == 0:
            result.append('Fizz')
        elif ele % 5 == 0:
            result.append('Buzz')
        else:
            result.append(ele)
    return result
    
    
class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        n = 10
        actual = fizzbuzz(n)
        self.assertEqual(actual, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz'])
