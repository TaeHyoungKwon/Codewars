import sys

from itertools import combinations

LOTTO_COUNT = 6


def solution(s: list[int]):
    result = []

    for combination in combinations(s, LOTTO_COUNT):
        result.append(" ".join(map(str, combination)))

    return "\n".join(result)


if __name__ == "__main__":
    for line in sys.stdin:
        if not line.strip():
            continue
        input_values = list(map(int, line.split()))
        k, *s = input_values
        if k == 0:
            break
        print(solution(s), end="\n\n")
