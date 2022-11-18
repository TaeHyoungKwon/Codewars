import sys


def solution():
    examinee, prize_count = [int(number) for number in input().split()]
    scores = list(map(int, sys.stdin.readline().split()))
    print(sorted(scores, reverse=True)[prize_count - 1])


if __name__ == "__main__":
    solution()