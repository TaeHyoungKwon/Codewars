import re
import unittest


def validate_code(code):
    return bool(re.search(r'^[1-3]\d+', str(code)))
    
    
class TestValidateCode(unittest.TestCase):
    def test_validate_code(self):
        self.assertTrue(validate_code(code=123))
        self.assertTrue(validate_code(code=321))
