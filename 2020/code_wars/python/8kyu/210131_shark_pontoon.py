import unittest


def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed //= 2
    if shark_distance / shark_speed > pontoon_distance / you_speed:
        return "Alive!"
    return "Shark Bait!"


class TestShark(unittest.TestCase):
    def test_shark_should_return_alive(self):
        self.assertEqual(shark(12, 50, 4, 8, True), "Alive!")

    def test_shark_should_return_shark_bait(self):
        self.assertEqual(shark(24, 0, 4, 8, True), "Shark Bait!")

    def test_shark_should_return_alice_second_case(self):
        self.assertEqual(shark(7, 55, 4, 16, True), "Alive!")
