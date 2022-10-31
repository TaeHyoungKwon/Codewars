import sys


def _input():
    result = []
    for _ in range(9):
        result.append(int(input()))
    return result


def solution():
    numbers = _input()
    max_value = max(numbers)
    max_value_index = numbers.index(max_value)
    return "\n".join([str(max(numbers)), str(max_value_index + 1)])


if __name__ == "__main__":
    print(solution())
