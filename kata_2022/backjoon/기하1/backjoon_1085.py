from math import sqrt


def solution():
    x, y, w, h = map(int, input().split())
    point_list = _get_point_list(h, w)
    return int(
        min(
            sqrt((target_x - x) ** 2 + (target_y - y) ** 2)
            for target_x, target_y in point_list
            if target_x != x or target_y != y
        )
    )


def _get_point_list(h, w):
    point_list = []
    for i in range(w + 1):
        point_list.append((i, 0))
        point_list.append((i, h))
    for i in range(h + 1):
        point_list.append((0, i))
        point_list.append((w, i))
    return point_list


if __name__ == "__main__":
    print(solution())
