def solution():
    m = int(input())
    n = int(input())
    target_ranges = list(range(m, n + 1))

    result = []
    number = 1
    while (target_number := number**2) <= n:
        if target_number in target_ranges:
            result.append(target_number)
        number += 1
    return f"{sum(result)} {min(result)}" if result else -1


if __name__ == "__main__":
    print(solution())
