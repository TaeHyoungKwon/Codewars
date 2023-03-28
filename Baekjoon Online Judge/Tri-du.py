def solution(a: int, b: int) -> int:
    return a if a > b else b


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
