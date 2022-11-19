def solution():
    temp = []
    while True:
        male, female = map(int, input().split())
        if male == 0 and female == 0:
            break
        temp.append(male + female)

    return "\n".join(map(str, temp))


if __name__ == "__main__":
    print(solution())
