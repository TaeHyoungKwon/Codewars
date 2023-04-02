def solution(numbers: list[int]) -> int:
    sorted_numbers = sorted(numbers)
    a, b, c = sorted_numbers
    part_1 = a**2 + b**2
    part_2 = c**2

    if part_1 == part_2:
        return 1

    if part_1 >= part_2 and a == b == c:
        return 2
    else:
        return 0


if __name__ == "__main__":
    print(solution(list(map(int, input().split()))))
