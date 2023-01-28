from math import ceil


def solution(r: int, c: int, n: int) -> int:
    return ceil(r / n) * ceil(c / n)


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
