def solution(
    x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int
) -> int:
    x_group = (x1, x2, x3, x4)
    y_group = (y1, y2, y3, y4)
    x_result = max(*x_group) - min(*x_group)
    y_result = max(*y_group) - min(*y_group)
    result = x_result if x_result > y_result else y_result
    return result**2


if __name__ == "__main__":
    print(solution(*map(int, input().split()), *map(int, input().split())))
