import enum
import unittest


class RPS(enum.Enum):
    ROCK = "rock"
    SCISSORS = "scissors"
    PAPER = "paper"


class RESULT(enum.Enum):
    DRAW = "Draw!"
    PLAYER_1_WON = "Player 1 won"
    PLAYER_2_WON = "Player 2 won"


def rps(p1, p2):
    result = {
        (RPS.SCISSORS.value, RPS.ROCK.value): RESULT.PLAYER_2_WON.value,
        (RPS.SCISSORS.value, RPS.PAPER.value): RESULT.PLAYER_1_WON.value,
        (RPS.PAPER.value, RPS.SCISSORS.value): RESULT.PLAYER_2_WON.value,
        (RPS.PAPER.value, RPS.ROCK.value): RESULT.PLAYER_1_WON.value,
        (RPS.ROCK.value, RPS.PAPER.value): RESULT.PLAYER_2_WON.value,
        (RPS.ROCK.value, RPS.SCISSORS.value): RESULT.PLAYER_1_WON.value,
        (RPS.ROCK.value, RPS.ROCK.value): RESULT.DRAW.value,
        (RPS.SCISSORS.value, RPS.SCISSORS.value): RESULT.DRAW.value,
        (RPS.PAPER.value, RPS.PAPER.value): RESULT.DRAW.value,
    }
    return result[(p1, p2)]


class TestRPS(unittest.TestCase):
    def test_should_return_draw_when_given_p1_and_p2_is_same(self):
        self.assertEqual(rps(RPS.SCISSORS.value, RPS.SCISSORS.value), RESULT.DRAW.value)

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
