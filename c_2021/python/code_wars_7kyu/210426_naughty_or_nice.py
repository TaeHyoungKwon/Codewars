import unittest


def get_nice_names(people):
    return [person["name"] for person in people if person["was_nice"]]


def get_naughty_names(people):
    return [person["name"] for person in people if not person["was_nice"]]


class TestSanta(unittest.TestCase):
    def test_get_nice_names_on_success(self):
        self.assertEqual(
            get_nice_names(
                people=[{"name": "Santa", "was_nice": True}, {"name": "Warrior reading this kata", "was_nice": True}]
            ),
            ["Santa", "Warrior reading this kata"],
        )

    def test_get_nice_names_on_empty_sequence(self):
        self.assertEqual(get_nice_names(people=[]), [])

    def test_get_naughty_names_on_success(self):
        self.assertEqual(get_naughty_names(people=[{"name": "xDranik", "was_nice": False}]), ["xDranik"])

    def test_get_anughty_names_on_empty_sequence(self):
        self.assertEqual(get_naughty_names(people=[]), [])






"""
문제
- 두개 함수를 만들어서, 1개는 nice 한 사람 이름을 리스트 형태로 출력하고, 하나는 나이스 하지 못한 사람 이름을 리스트형태로 출력한다
해결
- 함수를 두개 만든 후, was_nice가 True, False 인지 여부에 따라서 리스트를 만들어서 리턴한다.
조건
- people이 없으면, []를 리턴한다
절차
1. get_nice_name을 함수를 작성한다. was_nice가 True 인 이름으로 리스트를 만든다
2. get_naughty_name을 함수를 작성한다. was_nice가 False 인 이름으로 리스트를 만든다
3. edge case를 처리한다. -> empty sequence

"""