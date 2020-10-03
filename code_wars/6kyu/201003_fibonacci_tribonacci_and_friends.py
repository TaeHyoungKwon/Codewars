import unittest


def Xbonacci(signature, n):
    output, x = signature[:n], len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output
    
    
class TestXbonacci(unittest.TestCase):
    def test_should_fail(self):
        signature, n = [0, 0, 0, 0, 1], 10
        actual = Xbonacci(signature, n)
        self.assertEqual(actual, [0,0,0,0,1,1,2,4,8,16])
