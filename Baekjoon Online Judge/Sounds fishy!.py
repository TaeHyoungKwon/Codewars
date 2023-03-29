from enum import Enum


class Result(str, Enum):
    FISH_RISING = "Fish Rising"
    FISH_DIVING = "Fish Diving"
    CONSTANT_DEPTH = "Fish At Constant Depth"
    NO_FISH = "No Fish"


def solution(depth: list[int]) -> str:
    if len(set(depth)) == 1:
        return Result.CONSTANT_DEPTH.value

    all_cases = list(zip(depth, depth[1:]))
    if all(first < second for first, second in all_cases):
        return Result.FISH_RISING.value
    elif all(first > second for first, second in all_cases):
        return Result.FISH_DIVING.value
    else:
        return Result.NO_FISH.value


if __name__ == "__main__":
    print(solution([int(input()) for _ in range(4)]))
