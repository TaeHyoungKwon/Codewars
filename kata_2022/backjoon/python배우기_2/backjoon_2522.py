def solution():
    number = int(input())

    upper = [" " * (number - 1 * i) + "*" * i for i in range(1, number)]
    mid = ["*" * number]
    lower = [" " * i + "*" * (number - 1 * i) for i in range(1, number)]

    return "\n".join(upper + mid + lower)


if __name__ == "__main__":
    print(solution())
