import sys


def solution():
    case_count = int(sys.stdin.readline())

    result = []
    for _ in range(case_count):
        a, b = map(int, sys.stdin.readline().split())
        result.append(a + b)
    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
