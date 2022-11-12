from collections import Counter


def solution():
    x_points = []
    y_points = []
    for _ in range(3):
        x, y = map(int, input().split())
        x_points.append(x)
        y_points.append(y)

    least_x_point = Counter(x_points).most_common()[-1]
    least_y_point = Counter(y_points).most_common()[-1]

    return f"{least_x_point[0]} {least_y_point[0]}"


if __name__ == "__main__":
    print(solution())
