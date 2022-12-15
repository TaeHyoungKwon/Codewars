def solution():
    songchan_need_battery, teacher_battery = map(int, input().split())
    return int(songchan_need_battery == teacher_battery)


if __name__ == "__main__":
    print(solution())
