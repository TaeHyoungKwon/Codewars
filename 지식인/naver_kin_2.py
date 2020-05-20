import unittest


def solution():
    names = {}
    repeitition = int(input())
    value = 0
    for _ in range(repeitition):
        name = input()
        first_name = name.split()[-1]
        if first_name in names:
            names[first_name] += 1
        else:
            names[first_name] = value
    return names
    
    
class Test(unittest.TestCase):
    def test_should_fail(self):
        self.fail()
