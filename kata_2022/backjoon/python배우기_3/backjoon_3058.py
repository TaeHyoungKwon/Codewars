def solution():
    case_count = int(input())

    result = []
    for _ in range(case_count):
        numbers = list(map(int, input().split()))
        even_numbers = [number for number in numbers if number % 2 == 0]
        result.append(f"{sum(even_numbers)} {min(even_numbers)}")

    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
