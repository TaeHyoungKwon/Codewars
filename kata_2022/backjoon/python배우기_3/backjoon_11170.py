def solution():
    case_count = int(input())

    result = []
    for _ in range(case_count):
        start, end = map(int, input().split())
        numbers = "".join(
            str(number) for number in range(start, end + 1) if "0" in str(number)
        )
        result.append(numbers.count("0"))

    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
