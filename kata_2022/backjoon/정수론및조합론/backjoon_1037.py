def solution():
    case_count = int(input())
    numbers = [int(number) for number in input().split()]
    return min(numbers) * max(numbers)


if __name__ == "__main__":
    print(solution())
