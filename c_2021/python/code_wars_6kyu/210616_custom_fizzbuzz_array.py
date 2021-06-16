import itertools
import unittest
from typing import Generator, List, Union


# def fizz_buzz_custom(string_one="Fizz", string_two="Buzz", num_one=3, num_two=5):
#     result = []
#     for i in range(1, 101):
#         x = ""
#         if i % num_one == 0:
#             x += string_one
#         if i % num_two == 0:
#             x += string_two
#         result.append(x or i)
#     return result



def fizz_buzz_custom(
    string_one: str = "Fizz", string_two: str = "Buzz", num_one: int = 3, num_two: int = 5
) -> List[Union[int, str]]:
    def generate_fizz_buzz_custom() -> Generator:
        for num in itertools.count(1):
            if num == 101:
                break
            if num % num_one == 0 and num % num_two == 0:
                yield f"{string_one}{string_two}"
            elif num % num_one == 0:
                yield string_one
            elif num % num_two == 0:
                yield string_two
            else:
                yield num

    return list(generate_fizz_buzz_custom())


class TestFizzBuzzCustom(unittest.TestCase):
    def test_fizz_buzz_with_default(self):
        self.assertEqual(fizz_buzz_custom()[15], 16)
        self.assertEqual(fizz_buzz_custom()[44], "FizzBuzz")

    def test_fizz_buzz_with_custom(self):
        self.assertEqual(fizz_buzz_custom('Hey', 'There')[25], 26)
        self.assertEqual(fizz_buzz_custom("What's ", "up?", 3, 7)[80], "What's ")



"""
문제
* fizz_buzz sequence(3 or 5 의 배수에 각각 Fizz와 Buzz를 3과5의 공통된 배수에는 FizzBuzz로 출력 하는 sequence)를 주어진 인자에 따라서 커스텀 할 수 있도록 수정
해결
* 
조건
* input -> string_one:str = "Fizz", string_two:str = "Buzz", num_one: int = 3, num_two: int = 5 / output -> List[Union[int, str]]
절차
1. Fizz Buzz 기존 sequence를 구현해 본다
2. 1번의 구현에 맞게 인자에 다른 값이 들어올 때도 적용되도록 한다
테스트
1. Fizz Buzz 기본
2. 그외 케이스는 1가지
"""