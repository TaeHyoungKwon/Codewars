from datetime import timedelta


def solution():
    current_times = [int(ele) for ele in input().split(":")]
    target_times = [int(ele) for ele in input().split(":")]

    target_hours, target_minutes, target_seconds = target_times
    current_hours, current_minutes, current_seconds = current_times

    total_diff_seconds = (
        timedelta(
            hours=target_hours,
            minutes=target_minutes,
            seconds=target_seconds,
        )
        - timedelta(
            hours=current_hours,
            minutes=current_minutes,
            seconds=current_seconds,
        )
    ).seconds

    if total_diff_seconds < 0:
        total_diff_seconds += 3600 * 24

    hours = total_diff_seconds // 3600
    minutes = (total_diff_seconds % 3600) // 60
    seconds = total_diff_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


if __name__ == "__main__":
    print(solution())
