from typing import final

PIE: final = 3.141592


def solution(d1: int, d2: int) -> float:
    return 2 * d1 + 2 * PIE * d2


if __name__ == "__main__":
    d1 = int(input())
    d2 = int(input())

    print(solution(d1, d2))
