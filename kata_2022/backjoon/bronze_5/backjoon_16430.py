def solution():
    a, b = map(int, input().split())
    return " ".join(map(str, [(b - a), b]))


if __name__ == "__main__":
    print(solution())
