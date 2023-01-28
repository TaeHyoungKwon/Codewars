from dataclasses import dataclass
from enum import Enum


@dataclass
class BaseTeamScore:
    point_3: int
    point_2: int
    point_1: int

    def total_score(self):
        return self.point_3 * 3 + self.point_2 * 2 + self.point_1 * 1


@dataclass
class Apple(BaseTeamScore):
    ...


@dataclass
class Banana(BaseTeamScore):
    ...


class Result(str, Enum):
    APPLE_WIN = "A"
    BANANA_WIN = "B"
    TIE = "T"


def solution(apple_scores: list[int], banana_scores: list[int]):
    apple = Apple(*apple_scores).total_score()
    banana = Banana(*banana_scores).total_score()

    if apple > banana:
        return Result.APPLE_WIN.value
    elif apple < banana:
        return Result.BANANA_WIN.value
    else:
        return Result.TIE.value


if __name__ == "__main__":
    apple_3_point = int(input())
    apple_2_point = int(input())
    apple_1_point = int(input())

    banana_3_point = int(input())
    banana_2_point = int(input())
    banana_1_point = int(input())

    apple_scores = [apple_3_point, apple_2_point, apple_1_point]
    banana_scores = [banana_3_point, banana_2_point, banana_1_point]
    print(solution(apple_scores, banana_scores))
