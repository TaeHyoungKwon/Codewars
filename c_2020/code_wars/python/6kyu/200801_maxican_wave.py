import unittest


def wave(people):
    result = []
    for index, person in enumerate(people):
        if person == ' ':
            continue
        person_list = list(people)
        person_list[index] = person_list[index].upper()
        result.append(''.join(person_list))

    return result
    
    
class TestMaxicanWave(unittest.TestCase):
    def test_wave_with_hello(self):
        self.assertEqual(
            wave(people='hello'),
            ["Hello", "hEllo", "heLlo", "helLo", "hellO"],
        )

    def test_wave_with_gap(self):
        self.assertEqual(
            wave(people=' gap '),
            [' Gap ', ' gAp ', ' gaP '],
        )
