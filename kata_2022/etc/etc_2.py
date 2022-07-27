from datetime import datetime, timedelta


def solution(k, order_times):
    result = []
    for index, standard_time in enumerate(order_times, 1):
        cnt = 1
        for target_time in order_times[index:]:
            standard_time_for_datetime = datetime.strptime(standard_time, "%H:%M")
            standard_time_for_datetime += timedelta(minutes=k)

            hours = standard_time_for_datetime.hour
            minutes = standard_time_for_datetime.minute

            if minutes < 10:
                minutes = str(minutes).rjust(2, "0")

            if target_time <= f"{hours}:{minutes}":
                cnt += 1
        result.append(cnt)
    return max(result)


def test_solution():
    assert solution(1, ["12:10", "12:20", "12:40", "12:40", "12:50", "13:00", "13:20"]) == 2
    assert solution(20, ["12:10", "12:20", "12:40", "12:40", "12:50", "13:00", "13:20"]) == 4
    assert solution(25, ["12:10", "12:20", "12:40", "12:40", "12:50", "13:00", "13:20"]) == 4
    assert solution(12, ["12:10", "12:20", "12:40", "12:40", "12:50", "13:00", "13:20"]) == 3
    assert solution(30, ["12:10", "12:20", "12:40", "12:40", "12:50", "13:00", "13:20"]) == 4
    assert solution(120, ["12:10", "12:20", "12:40", "12:40", "12:50", "13:00", "13:20"]) == 7
