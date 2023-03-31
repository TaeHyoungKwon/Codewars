from math import ceil


def solution(height: int, target_height: int, tumor_growth: int):
    return ceil((target_height - height) / tumor_growth)


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
