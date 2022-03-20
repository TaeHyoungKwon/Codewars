from typing import Optional


def prev_mult_of_three(n: int) -> Optional[int]:
    n: list[int] = list(map(int, str(n)))
    for _ in range(len(n)):
        combined = int("".join(str(ele) for ele in n))
        if combined % 3 == 0:
            return combined
        n.pop()

    return None


class TestPrevMultOfThree:
    def test_prev_mult_of_three_on_result_is_none(self):
        assert prev_mult_of_three(n=1) is None
        assert prev_mult_of_three(n=25) is None

    def test_prev_mult_of_three_on_result_is_not_none(self):
        assert prev_mult_of_three(n=36) == 36
        assert prev_mult_of_three(n=1244) == 12
        assert prev_mult_of_three(n=952406) == 9


"""
Problem
    * Find a digit which is a multiple of three by removing the last digit until your're left with that
Solution
    * Solve problem step by step like below Steps
Conditions
    * Result is None
    * Result is not None
Steps
    1. Change n is just number to list by split digit
    2. Check rest elements in list is multiple of three or not
        * If False, Pop() last element from list and go to next loop
        * If True, return rest elements combined with int value
    3. If loop is end, should return None
Tests
    * Result is None
    * Result is not None
"""