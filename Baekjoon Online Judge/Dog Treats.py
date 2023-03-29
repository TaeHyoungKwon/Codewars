from enum import Enum


class MoodType(str, Enum):
    HAPPY = "happy"
    SAD = "sad"


def solution(s: int, m: int, l: int) -> str:
    formula = 1 * s + 2 * m + 3 * l
    return MoodType.HAPPY.value if formula >= 10 else MoodType.SAD.value


if __name__ == "__main__":
    numbers = {size: int(input()) for size in ["s", "m", "l"]}
    print(solution(**numbers))
