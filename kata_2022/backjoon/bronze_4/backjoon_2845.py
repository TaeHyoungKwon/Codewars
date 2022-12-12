def solution():
    l, p = map(int, input().split())
    people_count = map(int, input().split())
    result = map(lambda x: x + (-1 * l * p), people_count)
    return " ".join(map(str, result))


if __name__ == "__main__":
    print(solution())
