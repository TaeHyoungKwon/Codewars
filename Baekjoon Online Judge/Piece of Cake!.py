THICK = 4


def solution(n: int, h: int, v: int) -> int:
    return max(h, n - h) * max(v, n - v) * THICK


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
