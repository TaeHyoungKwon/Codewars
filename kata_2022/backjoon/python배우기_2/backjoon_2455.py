TRAIN_STATION_COUNT = 4


def solution():
    max_value = 0
    prev = 0
    for _ in range(TRAIN_STATION_COUNT):
        left_people, took_on_people = map(int, input().split())
        remainder = took_on_people - left_people
        total = prev + remainder
        if total > max_value:
            max_value = total
        prev = total

    return max_value


if __name__ == "__main__":
    print(solution())
