import sys


def solution():
    fixed, variable, price = map(int, sys.stdin.readline().split())

    if variable >= price:
        return -1
    else:
        return fixed // (price - variable) + 1


if __name__ == "__main__":
    print(solution())