import sys


def solution():
    while True:
        try:
            print(input())
        except EOFError:
            break


if __name__ == "__main__":
    solution()
