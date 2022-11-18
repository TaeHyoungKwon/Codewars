import sys


def solution():
    result = []
    while True:
        try:
            a, b = map(int, sys.stdin.readline().split())
        except:
            break
        else:
            result.append(a + b)
    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
