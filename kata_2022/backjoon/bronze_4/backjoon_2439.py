def solution():
    n = int(input())
    return "\n".join(" " * (n - i) + "*" * i for i in range(1, n + 1))


if __name__ == "__main__":
    print(solution())
