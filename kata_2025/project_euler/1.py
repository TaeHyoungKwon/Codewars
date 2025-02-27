"""
If we list all the natural numbers below 10
 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9.
 The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
- 3의 배수의 합 + 5의 배수의 합 - 15의 배수의 합 (중복 제거)
"""


def sum_multiples_of(target_number: int, divisor: int) -> int:
    last = ((target_number - 1) // divisor) * divisor
    count = last // divisor
    return (divisor + last) * count // 2


def sum_of_multiples(target_number: int, a: int, b: int) -> int:
    return (
        sum_multiples_of(target_number, a)
        + sum_multiples_of(target_number, b)  # 3의 배수의 합
        - sum_multiples_of(target_number, a * b)  # 5의 배수의 합  # 15의 배수의 합(중복 제거)
    )


if __name__ == "__main__":
    print(sum_of_multiples(1000, 3, 5))  # 1000 미만의 3 또는 5의 배수의 합
