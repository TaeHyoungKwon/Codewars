import sys


def solution():
    result = []
    while True:
        a, b = map(int, sys.stdin.readline().split())
        if a == 0 and b == 0:
            break
        result.append(a + b)
    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
