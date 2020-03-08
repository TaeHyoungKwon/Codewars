import unittest
import enum


class RPS(enum.Enum):
    ROCK = "rock"
    SCISSORS = "scissors"
    PAPER = "paper"


class RESULT(enum.Enum):
    DRAW = "Draw!"
    PLAYER_1_WON = "Player 1 won"
    PLAYER_2_WON = "Player 2 won"


def rps(p1, p2):
    if p1 == RPS.SCISSORS.value and p2 == RPS.ROCK.value:
        return RESULT.PLAYER_2_WON.value
    elif p1 == RPS.SCISSORS.value and p2 == RPS.PAPER.value:
        return RESULT.PLAYER_1_WON.value
    elif p1 == RPS.PAPER.value and p2 == RPS.SCISSORS.value:
        return RESULT.PLAYER_2_WON.value
    elif p1 == RPS.PAPER.value and p2 == RPS.ROCK.value:
        return RESULT.PLAYER_1_WON.value
    elif p1 == RPS.ROCK.value and p2 == RPS.PAPER.value:
        return RESULT.PLAYER_2_WON.value
    elif p1 == RPS.ROCK.value and p2 == RPS.SCISSORS.value:
        return RESULT.PLAYER_1_WON.value
    else:
        return RESULT.DRAW.value


class TestRPS(unittest.TestCase):
    def test_should_return_draw_when_given_p1_and_p2_is_same(self):
        self.assertEqual(rps(RPS.SCISSORS, RPS.SCISSORS), RESULT.DRAW.value)

    def test_should_return_player_2_won_when_given_p1_is_scissors_and_p2_is_rock(self):
        self.assertEqual(rps(RPS.SCISSORS.value, RPS.ROCK.value), RESULT.PLAYER_2_WON.value)

    def test_should_return_player_1_won_when_given_p1_is_scissors_and_p2_is_paper(self):
        self.assertEqual(rps(RPS.SCISSORS.value, RPS.PAPER.value), RESULT.PLAYER_1_WON.value)

    def test_should_return_player_2_won_when_given_p1_is_paper_and_p2_is_scissors(self):
        self.assertEqual(rps(RPS.PAPER.value, RPS.SCISSORS.value), RESULT.PLAYER_2_WON.value)

    def test_should_return_player_1_won_when_given_p1_is_paper_and_p2_is_rock(self):
        self.assertEqual(rps(RPS.PAPER.value, RPS.ROCK.value), RESULT.PLAYER_1_WON.value)

    def test_should_return_player_2_won_when_given_p1_is_rock_and_p2_is_paper(self):
        self.assertEqual(rps(RPS.ROCK.value, RPS.PAPER.value), RESULT.PLAYER_2_WON.value)

    def test_should_return_player_1_won_when_given_p1_is_rock_and_p2_is_scissors(self):
        self.assertEqual(rps(RPS.ROCK.value, RPS.SCISSORS.value), RESULT.PLAYER_1_WON.value)
