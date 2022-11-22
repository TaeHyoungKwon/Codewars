def solution():
    number = int(input())
    return int(sum(1.5 * i * (i + 1) for i in range(1, number + 1)))


if __name__ == "__main__":
    print(solution())
