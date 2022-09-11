"""
Problem
* Write a code that return the number of integers within the range(x to y) are divisible by k

Conditions
* input/output
    input
        x, y, k --> int
    output
        the number of integers within the range(x...y) that are divisible by k
* need O(log n) solution - input numbers can be too large

"""

"""
def divisible_count(x: int, y: int, k: int) -> int:
    return sum(True for number in range(x, y + 1) if number % k == 0)
"""

"""
from fractions import Fraction

def divisible_count(x,y,k):
    x += k - (x % k or k)
    return int(Fraction(y - x + k, k))
    
def divisible_count(x,y,k):
    upper = y//k
    lower = (x-1)//k
    return upper - lower
"""


def divisible_count(x: int, y: int, k: int) -> int:
    return sum(True for number in range(x, y + 1) if number % k == 0)


class TestDivisibleCount:
    def test_divisible_count(self):
        assert divisible_count(6, 11, 2) == 3
        assert divisible_count(11, 345, 17) == 20
        assert divisible_count(1, 200, 3) == 66
