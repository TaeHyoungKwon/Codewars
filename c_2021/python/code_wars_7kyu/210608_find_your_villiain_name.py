import datetime
import unittest


FIRST = [
    "The Evil",
    "The Vile",
    "The Cruel",
    "The Trashy",
    "The Despicable",
    "The Embarrassing",
    "The Disreputable",
    "The Atrocious",
    "The Twirling",
    "The Orange",
    "The Terrifying",
    "The Awkward",
]
LAST = [
    "Mustache",
    "Pickle",
    "Hood Ornament",
    "Raisin",
    "Recycling Bin",
    "Potato",
    "Tomato",
    "House Cat",
    "Teaspoon",
    "Laundry Basket",
]


def get_villain_name(birthdate):
    day, month, _ = birthdate.strftime("%d/%m/%Y").split("/")
    return f"{FIRST[int(month) - 1]} {LAST[int(day[-1])]}"


class TestGetVillainName(unittest.TestCase):
    def test_get_villain_name(self):
        self.assertEqual(
            get_villain_name(birthdate=datetime.datetime.strptime("1/1/2000", "%d/%m/%Y")), "The Evil Pickle"
        )


"""
문제
- birthdate를 받아서, 월일에 따라서, 적절한 이름을 만들어서 리턴해준다
해결
- birthdate를 /로 나눠서 월, 일을 불러온 다음에 해당하는 값을 first, last에서 받아서 문자열로 합친다
조건
- input -> birthdate: datetime, output -> str
절차
1. birthdate를 "/" 로 나눠서 월, 일을 걸러 낸다
2. 월 - 1 의 index에 해당하는 first name 과, 일의 last digit의 index에 해당하는 last name을 더해서 리턴해준다
테스트
- 다른 조건이 없어서 성공조건만 하면 될 것 같다
"""
