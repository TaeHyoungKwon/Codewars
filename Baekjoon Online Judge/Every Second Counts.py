from datetime import datetime, date, time


def solution(before_time: list[int], after_time: list[int]):
    result = datetime.combine(date.min, time(*after_time)) - datetime.combine(
        date.min, time(*before_time)
    )
    return result.seconds


if __name__ == "__main__":
    before_time = list(map(int, input().split(" : ")))
    after_time = list(map(int, input().split(" : ")))
    print(solution(before_time, after_time))
