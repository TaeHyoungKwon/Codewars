from datetime import timedelta


def solution(hh: int, mm: int) -> int:
    standard_time = timedelta(hours=9, minutes=0)
    target_time = timedelta(hours=hh, minutes=mm)

    time_diff = target_time - standard_time

    return time_diff.seconds // 60


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
