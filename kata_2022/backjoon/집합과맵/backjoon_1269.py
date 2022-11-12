import sys
from collections import Counter


def solution():
    first_case, second_case = map(int, input().split())
    first_target_set = {int(number) for number in sys.stdin.readline().split()}
    second_target_set = {int(number) for number in sys.stdin.readline().split()}

    return len(first_target_set - second_target_set) + len(second_target_set - first_target_set)


if __name__ == "__main__":
    print(solution())