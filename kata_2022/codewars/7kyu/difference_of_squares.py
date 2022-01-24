def difference_of_squares(n: int):
    sum_of_numbers = sum(range(1, n + 1))
    sum_of_squared_numbers = sum(number ** 2 for number in range(1, n + 1))
    return abs(sum_of_numbers ** 2 - sum_of_squared_numbers)


class TestDifferenceOfSquares:
    def test_difference_of_squares_on_n_is_1(self):
        assert difference_of_squares(n=1) == 0

    def test_difference_of_squares_on_n_is_2(self):
        assert difference_of_squares(n=2) == 4

    def test_difference_of_squares_on_n_is_5(self):
        assert difference_of_squares(n=5) == 170

"""
문제
    - 차이를 구해라
        - |1 ~ n 까지 합의 제곱 - 1~n 의 각 요소 제급의 합|
해결
    - 아래 조건에 따라서 답을 구한다
조건
    - 1 <= n <= 100
절차
구현 절차
1. n을 받아서, 1~n 까지 합을 구한다
2. 1~n 까지 요소 제곱의 합을 구한다
3. 1, 2번을 뺀 값의 절대값을 리턴한다

테스트
* 성공
1. 5 -> 170
2. 10 -> 2640
3. 100 -> 25164150
"""