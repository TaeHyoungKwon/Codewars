import sys


"""


3층 1호 -> 1명 3층 2호 -> 5명
2층 1호 -> 1명 2층 2호 -> 4명
1층 1호 -> 1명 1층 2호 -> 3명 1층 3호 -> 6명
0층 1호 -> 1명 0층 2호 -> 2명 -> 0층 3호 -> 3명


1 4 10 19 34
1 3 6 9 15
1 2 3 4 5
"""


def solution():
    """아직 못푼 문제"""
    case_count = int(sys.stdin.readline())

    result = []
    for _ in range(case_count):
        k = map(int, sys.stdin.readline())
        a = map(int, sys.stdin.readline())


    return "\n".join(str(number) for number in result)


if __name__ == "__main__":
    print(solution())