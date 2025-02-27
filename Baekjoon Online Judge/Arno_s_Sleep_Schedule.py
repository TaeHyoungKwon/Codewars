sleep_time = int(input())
alarm_time = int(input())

if sleep_time in {0, 1, 2, 3}:
    sleep_time += 24

print(abs(sleep_time - (alarm_time + 24)))
