import unittest


def truthy():
    return True


def falsey():
    return False


def _if(bool_, func1, func2):
    return func1() if bool_ else func2()
    
    
class TestIf(unittest.TestCase):
    def test_if_on_calling_func1(self):
        self.assertEqual(_if(True, truthy, falsey), True)

    def test_if_on_calling_func2(self):
        self.assertEqual(_if(False, truthy, falsey), False)
