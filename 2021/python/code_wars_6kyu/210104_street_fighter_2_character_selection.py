import unittest

FIGHTERS = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"],
]

OPTS = ["up", "down", "right", "left"]


def street_fighter_selection(fighters, initial_position, moves):
    row, column = initial_position
    result = []
    up, down, right, left = OPTS
    for move in moves:
        if move == left:
            column = move_left(column)
        elif move == right:
            column = move_right(column)
        elif move == up:
            row = move_up(row)
        elif move == down:
            row = move_down(row)
        result.append(fighters[row][column])
    return result


def move_left(column):
    return column + 5 if column == 0 else column - 1


def move_right(column):
    return column - 5 if column == 5 else column + 1


def move_up(row):
    return row if row == 0 else row - 1


def move_down(row):
    return row if row == 1 else row + 1


class TestStreetFighterSelection(unittest.TestCase):
    def test_street_fighter_selection_should_return_empty_list(self):
        self.assertEqual(street_fighter_selection(FIGHTERS, (0, 0), []), [])

    def test_street_fighter_selection_with_all_left(self):
        self.assertEqual(
            street_fighter_selection(FIGHTERS, (0, 0), ["left"] * 8),
            ["Vega", "Balrog", "Guile", "Blanka", "E.Honda", "Ryu", "Vega", "Balrog"],
        )

    def test_street_fighter_selection_with_all_right(self):
        self.assertEqual(
            street_fighter_selection(FIGHTERS, (0, 0), ["right"] * 8),
            ["E.Honda", "Blanka", "Guile", "Balrog", "Vega", "Ryu", "E.Honda", "Blanka"],
        )

    def test_street_fighter_selection_with_all_up_on_i_is_0(self):
        self.assertEqual(street_fighter_selection(FIGHTERS, (0, 0), ["up"] * 4), ["Ryu", "Ryu", "Ryu", "Ryu"])

    def test_street_fighter_selection_with_all_down_on_i_is_0(self):
        self.assertEqual(street_fighter_selection(FIGHTERS, (0, 0), ["down"] * 4), ["Ken", "Ken", "Ken", "Ken"])

    def test_street_fighter_selection_with_all_4_directions_clockwise_twice(self):
        self.assertEqual(
            street_fighter_selection(FIGHTERS, (0, 0), ["up", "left", "down", "right"] * 2),
            ["Ryu", "Vega", "M.Bison", "Ken", "Ryu", "Vega", "M.Bison", "Ken"],
        )

    def test_street_fighter_selection_should_cover_all_characters(self):
        self.assertEqual(
            street_fighter_selection(FIGHTERS, (0, 0), ["up"] + ["left"] * 6 + ["down"] + ["right"] * 6),
            [
                "Ryu",
                "Vega",
                "Balrog",
                "Guile",
                "Blanka",
                "E.Honda",
                "Ryu",
                "Ken",
                "Chun Li",
                "Zangief",
                "Dhalsim",
                "Sagat",
                "M.Bison",
                "Ken",
            ],
        )
