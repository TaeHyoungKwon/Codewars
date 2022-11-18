import sys


def _input():
    row_count, col_count = map(int, sys.stdin.readline().split())

    result_1 = []
    for _ in range(row_count):
        result_1.append(list(map(int, sys.stdin.readline().split())))

    result_2 = []
    for _ in range(row_count):
        result_2.append(list(map(int, sys.stdin.readline().split())))

    return result_1, result_2, row_count, col_count


def solution():
    result_1, result_2, row_count, col_count = _input()

    result = []

    for i in range(row_count):
        temp = []
        for j in range(col_count):
            temp.append(int(result_1[i][j]) + int(result_2[i][j]))
        result.append(temp)

    for row in result:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    solution()
