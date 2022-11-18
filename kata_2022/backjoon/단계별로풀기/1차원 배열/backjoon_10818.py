import sys


def _input():
    total_count = int(sys.stdin.readline())
    all_integers = list(map(int, sys.stdin.readline().split()))
    return total_count, all_integers


def solution():
    total_count, all_integers = _input()
    return f"{min(all_integers)} {max(all_integers)}"


if __name__ == "__main__":
    print(solution())
