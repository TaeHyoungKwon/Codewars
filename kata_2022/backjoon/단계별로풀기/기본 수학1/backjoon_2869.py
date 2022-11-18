import math
import sys


def solution():
    afternoon, night, tree_height = map(int, sys.stdin.readline().split())
    day = (tree_height - night) / (afternoon - night)
    return math.ceil(day)


if __name__ == "__main__":
    print(solution())
