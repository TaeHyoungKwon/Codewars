def solution(s: int, t: int, d: int) -> int:
    return d // (2 * s) * t


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
