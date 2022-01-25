def is_narcissistic(number: int) -> bool:
    number: str = str(number)
    return sum(int(digit) ** len(number) for digit in number) == int(number)


class TestNarcissistic:
    def test_is_narcissistic(self):
        assert is_narcissistic(number=153) is True

    def test_is_not_narcissistic(self):
        assert is_narcissistic(number=259) is False


"""
문제
 - 나르시스틱 숫자를 찾자
해결
 - 예제를 보고, 규칙을 찾아서 문제를 풀어보자
조건
 - input -> i: int, output -> bool
절차
workflow
1. i의 digit 개수를 센다
2. digit의 i 승을 합한다
3. 2번의 결과가 i와 같은지 체크한다
4. 같으면 True, 틀리면 False
테스트
1. True인 경우
2. False인 경우
"""