import string
import unittest

# 다 못품


def abacaba(k):
    initial_string = ''
    for idx, ele in enumerate(string.ascii_lowercase):
        initial_string = initial_string + ele + initial_string
        if k == idx + 1:
            return initial_string[idx]


class TestAbaCaba(unittest.TestCase):
    def test_should_return_a_when_given_k_is_1(self):
        # Given: Set k
        k = 1
        # When: Call aabacaba
        actual = abacaba(k)
        # Then: test should return 1
        self.assertEqual(actual, 'a')

    def test_should_return_b_when_given_k_is_2(self):
        # Given: Set k
        k = 2
        # When: Call abacaba
        actual = abacaba(k)
        # Then: test should return 1
        self.assertEqual(actual, 'b')

    def test_should_return_a_when_given_k_is_3(self):
        # Given: Set k
        k = 3
        # When: Call abacaba
        actual = abacaba(k)
        # Then: test should return 1
        self.assertEqual(actual, 'a')

    def test_should_return_c_when_given_k_is_12(self):
        # Given: Set k
        k = 12
        # When: Call abacaba
        actual = abacaba(k)
        # Then: test should return 1
        self.assertEqual(actual, 'c')
        