def solution():
    test_cases_count = int(input())

    result = []
    for _ in range(test_cases_count):
        first, second = map(int, input().split())
        result.append(first + second)

    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
