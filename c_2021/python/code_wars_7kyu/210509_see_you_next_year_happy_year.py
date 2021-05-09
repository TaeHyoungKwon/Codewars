import unittest
import itertools


def next_happy_year(year):
    def is_distinct(candidate_year):
        return len(set(str(candidate_year))) == 4
    return next(candidate_year for candidate_year in itertools.count(year + 1) if is_distinct(candidate_year))
    
    
class TestNextHappyYear(unittest.TestCase):
    def test_next_happy_year(self):
        self.assertEqual(next_happy_year(year=1001), 1023)



"""
문제
주어진 year에서 가장 가까운 Happy Year를 찾아라
-> Happy Year는 각 digit이 distinct 한 해를 말한다
해결
-> 주어진 year로 부터 1 씩 더해가면서, 각 digit이 distict 한지 확인한다 distict하면 return 한다
조건
1. input -> year: int, output -> int
2. 1000 <= y <= 9000

절차
1. itertools.count(1000) 객체를 만든 후, 루프를 돌면서, distict 한지 검사한다.(next)
2. disctict하다면, 바로 리턴한다
3. 1,2 수행을 위해서 disctinct 검사 함수를 inner function으로 만든다

테스트
"""