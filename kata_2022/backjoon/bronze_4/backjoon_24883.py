from enum import Enum


class Result(str, Enum):
    D2 = "Naver D2"
    WHALE = "Naver Whale"


def solution(alphabet: str) -> str:
    return Result.D2.value if alphabet.lower() == "n" else Result.WHALE.value


if __name__ == "__main__":
    print(solution(input()))
