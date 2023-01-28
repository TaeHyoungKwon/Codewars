def solution(n: int, m: int) -> int:
    return min([n, m]) // 2


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
