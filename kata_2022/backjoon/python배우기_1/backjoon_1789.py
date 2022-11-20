def solution():
    s = int(input())
    n = 1
    while n * (n + 1) / 2 <= s:
        n += 1
    return n - 1


if __name__ == "__main__":
    print(solution())
