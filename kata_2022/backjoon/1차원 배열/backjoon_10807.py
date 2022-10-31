import sys


def _input():
    total_count = int(sys.stdin.readline())
    all_integers = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    return total_count, all_integers, target


def solution():
    total_count, all_integers, target = _input()
    return all_integers.count(target)


if __name__ == "__main__":
    print(solution())
