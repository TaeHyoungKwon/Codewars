import sys


def solution():
    m, n = map(int, sys.stdin.readline().split())

    for number in range(m, n + 1):
        if _is_prime(number):
            print(number)


def _is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    solution()
