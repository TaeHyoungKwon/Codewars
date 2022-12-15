def solution():
    soongsil, korea, hanyang = map(int, input().split())

    participation_level_map = {"soongsil": soongsil, "korea": korea, "hanyang": hanyang}

    if sum(participation_level_map.values()) >= 100:
        return "OK"

    university_need_to_pressure = sorted(
        participation_level_map.items(), key=lambda x: x[1]
    )[0][0]

    return university_need_to_pressure.title()


if __name__ == "__main__":
    print(solution())
