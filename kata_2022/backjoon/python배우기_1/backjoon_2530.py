def solution():
    hours, minutes, seconds = map(int, input().split())
    additional_seconds = int(input())

    result = []
    for standard_second in [3600, 60, 1]:
        if additional_seconds >= standard_second:
            quotient, remainder = divmod(additional_seconds, standard_second)
            result.append(quotient)
            additional_seconds = remainder
        else:
            result.append(0)
    a_hours, a_minutes, a_seconds = result

    total_seconds = seconds + a_seconds
    total_minutes = minutes + a_minutes + total_seconds // 60
    total_hours = (hours + a_hours + total_minutes // 60) % 24

    return f"{total_hours} {total_minutes % 60} {total_seconds % 60}"


if __name__ == "__main__":
    print(solution())
