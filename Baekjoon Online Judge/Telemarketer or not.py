from enum import Enum


class Result(str, Enum):
    IGNORE = "ignore"
    Answer = "answer"


def solution(last_four_digits: str) -> str:
    first = last_four_digits[0]
    last = last_four_digits[3]

    target = {"8", "9"}

    if first in target and last in target and last_four_digits[1] == last_four_digits[2]:
        return Result.IGNORE.value
    return Result.Answer.value


if __name__ == "__main__":
    print(solution("".join(input() for _ in range(4))))
