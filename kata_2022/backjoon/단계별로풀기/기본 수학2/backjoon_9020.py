import sys


def solution():
    case_count = int(sys.stdin.readline())

    for _ in range(case_count):
        even_number_n = int(sys.stdin.readline())

        a, b = even_number_n // 2, even_number_n // 2
        while a > 0:
            if _is_prime(a) and _is_prime(b):
                print(a, b)
                break
            else:
                a -= 1
                b += 1


def _is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    solution()
