def solution():
    numbers = input().split(",")
    return sum(number.isnumeric() for number in numbers)


if __name__ == "__main__":
    print(solution())
