def solution():
    phy = int(input())
    chem = int(input())
    bio = int(input())
    earth = int(input())
    history = int(input())
    geo = int(input())
    return sum(sorted([phy, chem, bio, earth], reverse=True)[:3]) + max(history, geo)


if __name__ == "__main__":
    print(solution())
