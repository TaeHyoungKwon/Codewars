def solution():
    n1, n2, n12 = map(int, input().split())
    return (n1 + 1) * (n2 + 1) // (n12 + 1) - 1


if __name__ == "__main__":
    print(solution())
