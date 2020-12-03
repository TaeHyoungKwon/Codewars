import math
import unittest


def movie(card, ticket, perc):
    prev = ticket * perc
    i = 1
    temp = prev
    while ticket * i < math.ceil(card + temp):
        prev = prev * perc
        temp += prev
        i += 1
    return i


class TestMovie(unittest.TestCase):
    def test_movie_first_case(self):
        self.assertEqual(movie(card=500, ticket=15, perc=0.9), 43)

    def test_movie_second_case(self):
        self.assertEqual(movie(card=100, ticket=10, perc=0.95), 24)
