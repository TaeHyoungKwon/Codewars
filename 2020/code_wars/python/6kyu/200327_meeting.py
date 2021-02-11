import unittest


def meeting(s):
    full_name_set = [(ele.split(":")[1].upper(), ele.split(":")[0].upper()) for ele in s.split(";")]
    return "".join(
        "({}, {})".format(last_name, first_name)
        for last_name, first_name in sorted(full_name_set, key=lambda x: (x[0], x[1]))
    )


class TestMeeting(unittest.TestCase):
    def test_meeting(self):
        s = "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
        actual = meeting(s)
        self.assertEqual(
            actual,
            "(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)",
        )
