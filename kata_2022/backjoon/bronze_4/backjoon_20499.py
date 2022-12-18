def solution(k: int, d: int, a: int) -> str:
    return "hasu" if k + a < d or d == 0 else "gosu"


if __name__ == "__main__":
    print(solution(*map(int, input().split("/"))))
