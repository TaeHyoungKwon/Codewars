def solution():
    case_count = int(input())
    total = 0
    for _ in range(case_count):
        apple_count, student_count = map(int, input().split())
        _, remainder = divmod(student_count, apple_count)
        total += remainder
    return total


if __name__ == "__main__":
    print(solution())
