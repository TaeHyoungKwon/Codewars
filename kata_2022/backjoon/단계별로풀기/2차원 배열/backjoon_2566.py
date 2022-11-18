import sys


def _input():
    result = []
    for _ in range(9):
        result.append(list(map(int, sys.stdin.readline().split())))
    return result


def solution():
    table = _input()
    prev_max_value = -1
    t_row, t_col = 0, 0

    for index, row in enumerate(table, 1):
        target_max_value = max(row)
        if target_max_value > prev_max_value:
            prev_max_value = max(row)
            t_row = index
            t_col = row.index(prev_max_value) + 1

    print(prev_max_value)
    print(f"{t_row} {t_col}")


if __name__ == "__main__":
    solution()
