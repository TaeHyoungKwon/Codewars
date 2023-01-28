from enum import Enum


class Result(str, Enum):
    YES = "YES"
    NO = "NO"


def solution(expression: str) -> str:
    a, b, c = [int(element) for element in expression.split() if element.isnumeric()]
    return Result.YES.value if a + b == c else Result.NO.value


if __name__ == "__main__":
    print(solution(input()))
