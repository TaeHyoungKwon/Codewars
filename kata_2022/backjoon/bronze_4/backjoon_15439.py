from itertools import combinations


def solution():
    n = int(input())
    return len(list(combinations(range(n), 2))) * 2


if __name__ == "__main__":
    print(solution())
