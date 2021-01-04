import unittest


def switch_it_up(number):
    numbers = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', "Nine")
    return {index: word for index, word in enumerate(numbers)}[number]
    
    
class TestSwitchItUp(unittest.TestCase):
    def test_should_return_zero_when_given_number_is_0(self):
        number = 0
        actual = switch_it_up(number)
        self.assertEqual(actual, 'Zero')

    def test_should_return_nine_when_given_number_is_9(self):
        number = 9
        actual = switch_it_up(number)
        self.assertEqual(actual, 'Nine')
