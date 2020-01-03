import unittest

'''
1. 리스트 안에 주어진 int 조건 말고 다른 값이 있을 때, 무조건 false
2. 리스트가 비었을 때, True
3. int이거나 float 인데, no decimal 일  -> 0으로 끝나는 float 
'''


def is_int_array(arr):
    if arr is None:
        return False
    if arr == '':
        return False
    if not arr:
        return True
    if None in arr:
        return False
    return all(float(ele).is_integer() for ele in arr)
    
    
class TestIsIntArray(unittest.TestCase):
    def test_should_return_true_given_arr_is_empty(self):
        # Given: Set arr
        arr = []
        # When: Call is_int_array
        actual = is_int_array(arr)
        # Then: is_int_array should return True
        self.assertEqual(actual, True)

    def test_should_return_false_given_arr_has_none(self):
        # Given: Set arr
        arr = [1, 2, 3, None]
        # When: Call is_int_array
        actual = is_int_array(arr)
        # Then: is_int_array should return False
        self.assertEqual(actual, False)

    def test_should_return_true_given_arr_has_only_integer_num(self):
        # Given: Set arr
        arr = [1, 2, 3]
        # When: Call is_int_array
        actual = is_int_array(arr)
        # Then: is_int_array should return True
        self.assertEqual(actual, True)

    def test_should_return_true_given_arr_is_empty_string(self):
        # Given: Set arr
        arr = ''
        # When: Call is_int_array
        actual = is_int_array(arr)
        # Then: is_int_array should return False
        self.assertEqual(actual, False)

    def test_should_return_false_given_arr_is_none(self):
        # Given: Set None
        arr = None
        # When: Call is_int_array
        actual = is_int_array(arr)
        # Then: is_int_array should return False
        self.assertEqual(actual, False)

    def test_should_return_false_given_arr_has_float_with_decimal(self):
        # Given: Set arr
        arr = [1.0, 2.0, 3.0001]
        # When: Call is_int_array
        actual = is_int_array(arr)
        # Then: is_int_array should return False
        self.assertEqual(actual, False)

    def test_should_return_false_given_arr_string_type(self):
        # Given: Set arr
        arr = ['-1']
        # When: Call is_int_array
        actual = is_int_array(arr)
        # Then: is_int_array should return False
        self.assertEqual(actual, False)
        