import unittest

TWENTY_FIVE_DOLLAR = 25
FIFTY_DOLLAR = 50
ONE_HUNDRED_DOLLAR = 100

NO = "NO"
YES = "YES"


def tickets(people):
    income = []

    for bill in people:
        if bill == FIFTY_DOLLAR:
            if TWENTY_FIVE_DOLLAR not in income:
                return 'NO'
            income.remove(TWENTY_FIVE_DOLLAR)
            income.append(FIFTY_DOLLAR)

        elif bill == ONE_HUNDRED_DOLLAR:
            if TWENTY_FIVE_DOLLAR in income and FIFTY_DOLLAR in income:
                income.remove(TWENTY_FIVE_DOLLAR)
                income.remove(FIFTY_DOLLAR)
                income.append(ONE_HUNDRED_DOLLAR)
            elif income.count(TWENTY_FIVE_DOLLAR) == 3:
                income.remove(TWENTY_FIVE_DOLLAR)
                income.remove(TWENTY_FIVE_DOLLAR)
                income.remove(TWENTY_FIVE_DOLLAR)
                income.append(ONE_HUNDRED_DOLLAR)
            else:
                return 'NO'
        else:
            income.append(TWENTY_FIVE_DOLLAR)

    return "YES"


class TestTickets(unittest.TestCase):
    def test_tickets_on_yes(self):
        people = [25, 25, 50]
        actual = tickets(people)
        self.assertEqual(actual, "YES")

    def test_tickets_on_no(self):
        people = [25, 100]
        actual = tickets(people)
        self.assertEqual(actual, "NO")

    def test_tickets_on_no_case_two(self):
        people = [25, 25, 50, 50, 100]
        actual = tickets(people)
        self.assertEqual(actual, "NO")

    def test_tickets_on_yes_case_two(self):
        people = [25, 25, 50, 100]
        actual = tickets(people)
        self.assertEqual(actual, "YES")

    def test_tickets_on_yes_edge_case(self):
        people = [25, 25, 25, 25, 50, 100, 50]
        actual = tickets(people)
        self.assertEqual(actual, "YES")
