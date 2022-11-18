def solution():
    first = int(input())
    second = int(input())

    if first > 0 and second > 0:
        return 1
    elif first < 0 and second > 0:
        return 2
    elif first < 0 and second < 0:
        return 3
    else:
        return 4


if __name__ == "__main__":
    print(solution())