from datetime import timedelta


def _get_total_seconds(working_time):
    start_h, start_m, start_s, end_h, end_m, end_s = working_time
    return (
        timedelta(hours=end_h, minutes=end_m, seconds=end_s)
        - timedelta(hours=start_h, minutes=start_m, seconds=start_s)
    ).seconds


def _get_time(total_seconds):
    hour, remainder = divmod(total_seconds, 3600)
    minute, second = divmod(remainder, 60)
    return hour, minute, second


def solution():
    result = []
    for _ in range(3):
        total_seconds = _get_total_seconds(
            working_time=[int(time_element) for time_element in input().split()]
        )
        hour, minute, second = _get_time(total_seconds)
        result.append(f"{hour} {minute} {second}")
    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
