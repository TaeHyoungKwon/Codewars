import unittest


def gcdi(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


def lcmu(a, b):
    return abs(a * b) // gcdi(a, b)


def som(a, b):
    return a + b


def maxi(a, b):
    return max(a, b)


def mini(a, b):
    return min(a, b)


def oper_array(fct, arr, init):
    temp = []
    for ele in arr:
        init = fct(init, ele)
        temp.append(init)
    return temp


class TestEachFunction(unittest.TestCase):
    common_input = [18, 69, -90, -78, 65, 40]

    def test_gcdi(self):
        self.assertEqual(gcdi(x=10, y=20), 10)

    def test_lcmu(self):
        self.assertEqual(lcmu(a=4, b=20), 20)

    def test_som(self):
        self.assertEqual(som(a=4, b=20), 24)

    def test_maxi(self):
        self.assertEqual(maxi(a=10, b=20), 20)

    def test_mini(self):
        self.assertEqual(mini(a=10, b=20), 10)

    def test_oper_array(self):
        self.assertEqual(oper_array(som, self.common_input, 0), [18, 87, -3, -81, -16, 24])

    def test_oper_array_with_gcdi(self):
        self.assertEqual(oper_array(gcdi, self.common_input, 0), [18, 3, 3, 3, 1, 1])
