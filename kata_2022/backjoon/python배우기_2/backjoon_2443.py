def solution():
    number = int(input())
    return "\n".join(
        " " * (i - 1) + "*" * (-2 * i + (2 * number + 1)) for i in range(1, number + 1)
    )


if __name__ == "__main__":
    print(solution())
