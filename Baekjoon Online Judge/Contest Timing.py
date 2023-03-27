from datetime import datetime


def solution(day: int, hours: int, minutes: int) -> int:
    standard_day = datetime(2011, 11, 11, 11, 11)
    target_day = datetime(2011, 11, day, hours, minutes)

    diff = target_day - standard_day

    return int(result / 60) if (result := diff.total_seconds()) >= 0 else -1


if __name__ == "__main__":
    print(solution(*list(map(int, input().split()))))
