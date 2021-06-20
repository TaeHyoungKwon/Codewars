from typing import List
import unittest



class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)


def most_money(students: List[Student]):
    result = {student.name: student.fives * 5 + student.tens * 10 + student.twenties * 20 for student in students}
    sort_with_reversed = sorted(result.values(), reverse=True)
    if len(sort_with_reversed) > 1 and all(sort_with_reversed[0] == ele for ele in sort_with_reversed):
        return "all"
    return next(k for k, v in result.items() if v == sort_with_reversed[0])
    
    
class TestMostMoney(unittest.TestCase):
    def test_most_money_with_person_name(self):
        self.assertEqual(most_money(students=[cam, geoff, phil]), "Phil")

    def test_most_money_with_all_person_same(self):
        self.assertEqual(most_money(students=[cam, geoff]), "all")


"""
문제
* 주어진 students 정보를 보고, 가장 돈이 많은 사람 이름을 리턴
해결
* students instance list 루프를 돌면서, 돈의 합이 가장 큰 사람의 이름을 리턴
조건
* 1등은 무조건 1명이다
input -> students: List[Student], output -> str
절차
1. students를 루프를 돈다
2. 루프를 돌면서, fives, tens, twenties의 총 합을 더하여서, key, value 형태의 dict 를 만들다
3. 루프가 다 돌았을 때, 키가 가장 큰 이름을 리턴한다
테스트
1. 모두 같을 때, -> all
2. 1명의 most가 있을 때, -> 해당하는 이름

"""