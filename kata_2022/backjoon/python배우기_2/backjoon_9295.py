def solution():
    case_count = int(input())
    result = []
    for i in range(1, case_count + 1):
        first, second = map(int, input().split())
        result.append(f"Case {i}: {first + second}")
    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
