def solution():
    hour, minute = map(int, input().split())
    additional_minute = int(input())

    total_minute = minute + additional_minute
    if total_minute >= 60:
        additional_hour = total_minute // 60
        total_minute %= 60

        total_hour = hour + additional_hour
        if total_hour >= 24:
            total_hour -= 24
        return f"{total_hour} {total_minute}"
    else:
        return f"{hour} {total_minute}"


if __name__ == "__main__":
    print(solution())