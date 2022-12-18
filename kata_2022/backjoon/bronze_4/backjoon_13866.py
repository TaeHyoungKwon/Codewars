def solution(a: int, b: int, c: int, d: int) -> int:
    return abs((a + d) - (b + c))


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
