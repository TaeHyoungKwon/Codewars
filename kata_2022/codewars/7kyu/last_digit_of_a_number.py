def solution(n, d):
    if d <= 0:
        return []
    return list(map(int, str(n)))[-d:]


class TestSolution:
    def test_solution_with_common_cases(self):
        assert solution(n=12345, d=3) == [3, 4, 5]
        assert solution(n=12345, d=4) == [2, 3, 4, 5]
        assert solution(n=12345, d=5) == [1, 2, 3, 4, 5]

    def test_solution_with_special_cases(self):
        assert solution(n=1, d=334) == [1]
        assert solution(n=1, d=-1) == []
        assert solution(n=1234, d=0) == []



"""
Problem
    * Implenet a function whtich returns the last 'd' digists of an integer N from a list that made by 'n'
Solution
    * Solve each steps below
Conditions
    * common cases
        * 
    * special cases
        * d > n -> d is more than n
        * d <= 0 -> d is negative number;
Steps
    0. Check validation -> above special cases
    1. Change int type to list type that split by digit - ex) n = 123 -> [1, 2, 3]
    2. Slice list that we made with d with negative is start position - ex) n = 123, d = 3 -> [1, 2, 3][-3:]
    3. Return result

Test
    1. common cases
        1. d < n
        2. d > 0
    2. special cases
        1. d > n
        2. d <= 0
"""