import sys


def solution():
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    result = []
    for number in range(m, n + 1):
        if _is_prime(number):
            result.append(number)

    if result:
        print(sum(result))
        print(min(result))
    else:
        print(-1)


def _is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    solution()
