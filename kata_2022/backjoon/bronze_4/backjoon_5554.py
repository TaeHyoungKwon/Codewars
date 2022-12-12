def solution():
    home_to_school_seconds = int(input())
    school_to_pc_room_seconds = int(input())
    pc_room_to_academy_seconds = int(input())
    academy_to_home_seconds = int(input())

    total_seconds = (
        home_to_school_seconds
        + school_to_pc_room_seconds
        + pc_room_to_academy_seconds
        + academy_to_home_seconds
    )

    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}\n{seconds}"


if __name__ == "__main__":
    print(solution())
