import sys
from collections import Counter


def solution():
    case_count = int(sys.stdin.readline())
    numbers = sorted(int(sys.stdin.readline()) for _ in range(case_count))

    print(_get_arithmetic_mean(numbers))
    print(_get_median(numbers))
    print(_get_mode(numbers))
    print(_get_diff_between_max_n_min(numbers))


def _get_arithmetic_mean(numbers: list[int]) -> int:
    return round(sum(numbers) / len(numbers))


def _get_median(numbers: list[int]) -> int:
    return numbers[len(numbers) // 2]


def _get_mode(numbers: list[int]) -> int:
    cnt_result = Counter(numbers).most_common(2)
    if len(numbers) > 1:
        if cnt_result[0][1] == cnt_result[1][1]:
            return cnt_result[1][0]
        else:
            return cnt_result[0][0]
    else:
        return cnt_result[0][0]


def _get_diff_between_max_n_min(numbers: list[int]) -> int:
    return max(numbers) - min(numbers)


if __name__ == "__main__":
    solution()
