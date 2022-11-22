def solution():
    number = int(input())

    upper = [" " * (number - i) + "*" * (2 * (i - 1) + 1) for i in range(1, number)]
    mid = ["*" * (2 * number - 1)]
    lower = [" " * j + "*" * (-2 * j + (number * 2 - 1)) for j in range(1, number)]

    return "\n".join(upper + mid + lower)


if __name__ == "__main__":
    print(solution())
