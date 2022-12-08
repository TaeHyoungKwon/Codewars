def solution():
    a, b = map(int, input().split())
    defense_rate = a * (100 - b) / 100
    return int(defense_rate < 100)


if __name__ == "__main__":
    print(solution())
