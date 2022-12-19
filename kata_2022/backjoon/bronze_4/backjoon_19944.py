def solution(n: int, m: int) -> str:
    if m == 1 or m == 2:
        return "NEWBIE!"
    elif m <= n:
        return "OLDBIE!"
    else:
        return "TLE!"


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
