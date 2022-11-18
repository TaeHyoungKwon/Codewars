import sys


def solution():
    case_count = int(sys.stdin.readline())

    result = []
    for index in range(1, case_count + 1):
        a, b = map(int, sys.stdin.readline().split())
        result.append(f"Case #{index}: {a + b}")

    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
