from typing import Annotated

LowerCase = Annotated[str, "alphabet lowercase"]


def solution(name: str) -> LowerCase:
    return name.lower()


if __name__ == "__main__":
    case_count = int(input())
    for _ in range(case_count):
        print(solution(name=input()))
