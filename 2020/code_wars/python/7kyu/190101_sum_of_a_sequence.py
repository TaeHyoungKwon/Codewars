import unittest


def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number + 1, step))


class TestSequenceSum(unittest.TestCase):
    def test_should_return_0_when_begin_is_greater_than_end(self):
        # Given: Set begin_number, end_number, step
        begin_number, end_number, step = 16, 15, 2
        # When: Call sequence_sum
        actual = sequence_sum(begin_number, end_number, step)
        # Then: sequence_sum should return 0
        self.assertEqual(actual, 0)

    def test_should_return_45_when_begin_is_0_end_is_15_step_is_3(self):
        # Given: Set begin_number, end_number, step
        begin_number, end_number, step = 0, 15, 3
        # When: Call sequence_sum
        actual = sequence_sum(begin_number, end_number, step)
        # Then: sequence_sum should return 0
        self.assertEqual(actual, 45)
