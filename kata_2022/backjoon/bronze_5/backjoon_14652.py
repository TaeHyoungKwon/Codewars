def solution():
    n, m, target_number = map(int, input().split())
    q, r = divmod(target_number, m)
    return f"{q} {r}"


if __name__ == "__main__":
    print(solution())
