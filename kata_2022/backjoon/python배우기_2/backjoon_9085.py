def solution():
    case_count = int(input())
    result = []
    for _ in range(case_count):
        number_count = int(input())
        numbers = map(int, input().split())
        result.append(sum(numbers))
    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
