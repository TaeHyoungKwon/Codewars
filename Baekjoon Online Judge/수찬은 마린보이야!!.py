# 15921

from collections import Counter


class ZeroExpectedValueError(Exception):
    ...


def solution(count: int, sequence: list[int]) -> str:
    counter = Counter(sequence)
    expected_value = sum(k * (v / count) for k, v in counter.items())

    if expected_value == 0:
        raise ZeroExpectedValueError("기대 값이 0 입니다.")

    return f"{round((sum(sequence) / count) / expected_value, 2):.2f}"


if __name__ == "__main__":
    try:
        count = int(input())
        sequence = list(map(int, input().split()))
    except (EOFError, ZeroExpectedValueError):
        print("divide by zero")
    else:
        print(solution(count, sequence))
