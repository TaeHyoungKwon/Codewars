import math


def solution(area: int):
    return f"{math.sqrt(area) * 4}"


if __name__ == "__main__":
    print(solution(int(input())))
