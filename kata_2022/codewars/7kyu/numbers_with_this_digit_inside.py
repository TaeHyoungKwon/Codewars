from functools import reduce


def numbers_with_digit_inside(x: int, d: int) -> list[int]:
    numbers_with_digit_inside_list: list[int] = [number for number in range(1, x + 1) if str(d) in str(number)]

    number_count = len(numbers_with_digit_inside_list)
    number_sum = sum(numbers_with_digit_inside_list)
    number_product = number_count and reduce(lambda x, y: x * y, numbers_with_digit_inside_list)

    return [number_count, number_sum, number_product]


class TestNumbersWithDigitInside:
    def test_on_fail_case(self):
        assert numbers_with_digit_inside(x=5, d=6) == [0, 0, 0]

    def test_on_success_case(self):
        assert numbers_with_digit_inside(x=11, d=1) == [3, 22, 110]



"""
문제
- d 에 해당하는 digit이 을 가진 숫자를 1~x 범위에서 추출 한 후, 조건에 맞게 리스트로 리턴해야 한다
해결
- 아래 조건에 맞게 리스트 내 element 기준으로 리턴한다.
조건
- input/output
    1. input
        - x: int, d: int
    2. output
        - list[int]
        - index
            - 0: 갯수
            - 1: 리스트 요소의 합
            - 2: 리스트 요소의 곱
- 제약 조건
    1. digit에 해당하는 숫자가 없으면, [0, 0, 0]을 리턴한다
절차
- Workflow
    1. 1~x 까지 범위를 range 로 구한다
    2. 루프를 돌면서, digit에 해당하는 것들을 필터 한다
    3. 필터한 결과 값들을 output list 조건에 맞게 계산해서 리턴한다
테스트
1. 성공
    - 보통 케이스
2. 실패
    - 범위 내에 digit이 없는 경우
"""