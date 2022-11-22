def solution():
    case_count = int(input())

    result = []
    for _ in range(case_count):
        v, e = map(int, input().split())
        result.append(2 - v + e)

    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
