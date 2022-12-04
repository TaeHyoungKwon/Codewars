SPEED_FOR_MINUTE = 5


def solution():
    distance = int(input())
    q, r = divmod(distance, SPEED_FOR_MINUTE)

    return q + 1 if r else q


if __name__ == "__main__":
    print(solution())
