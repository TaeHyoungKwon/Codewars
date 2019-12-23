import unittest


def is_valid_IP(strng):
    if not strng or ',' in strng:
        return False
    for ele in strng.split('.'):
        if ele.isalpha():
            return False
        if int(ele) < 0 or int(ele) > 255:
            return False
        if ele[0] == '0' and len(ele) != 1:
            return False
        if len(strng.split('.')) != 4:
            return False
        if ' ' in ele:
            return False
    return True


class TestIpValidation(unittest.TestCase):
    def test_should_return_false_when_string_is_empty(self):
        string = ''
        result = is_valid_IP(string)
        self.assertFalse(result)

    def test_should_false_when_splited_string_length_is_not_four(self):
        string = '123.345.456.567.334'
        result = is_valid_IP(string)
        self.assertFalse(result)

    def test_should_false_when_splited_element_is_more_than_255(self):
        string = '0.0.0.256'
        result = is_valid_IP(string)
        self.assertFalse(result)

    def test_should_false_when_splited_element_is_less_than_0(self):
        string = '-1.-1.-1.255'
        result = is_valid_IP(string)
        self.assertFalse(result)

    def test_should_false_when_splitted_element_of_first_element_is_0(self):
        string = '01.02.03.04'
        result = is_valid_IP(string)
        self.assertFalse(result)

    def test_should_false_when_splitted_element_is_alphabet(self):
        string = 'ab.cd.ef.fg'
        result = is_valid_IP(string)
        self.assertFalse(result)

    def test_should_false_when_splitted_element_has_empty_space(self):
        string = 'ab.cd.ef  .fg'
        result = is_valid_IP(string)
        self.assertFalse(result)

    def test_should_false_when_splitted_element_by_comma(self):
        string = 'ab,cd,ef,fg'
        result = is_valid_IP(string)
        self.assertFalse(result)