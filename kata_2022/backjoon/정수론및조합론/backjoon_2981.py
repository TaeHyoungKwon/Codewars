def solution():
    # 못품: 시간초과A
    case_count = int(input())
    numbers = [int(input()) for _ in range(case_count)]

    result = []
    for index in range(2, max(numbers) + 1):
        if len(set(number % index for number in numbers)) == 1:
            result.append(index)

    return " ".join(str(number) for number in result)


if __name__ == "__main__":
    print(solution())
