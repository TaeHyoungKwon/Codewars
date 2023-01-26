def solution(n: int, m: int) -> int:
    return n * m // 2


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solution(n, m))
