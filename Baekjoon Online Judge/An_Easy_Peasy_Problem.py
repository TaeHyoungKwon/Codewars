solved_people, total_people = map(int, input().split())

if (solved_people / total_people) >= 0.5:
    print("E")
else:
    print("H")
