import re
from enum import Enum


class Result(str, Enum):
    YES = "YES"
    NO = "NO"


def solution(number: str) -> str:
    return Result.YES.value if re.match(r"^555\d{4}$", number) else Result.NO.value


if __name__ == "__main__":
    print(solution(input()))
