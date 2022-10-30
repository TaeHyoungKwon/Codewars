def solution():
    values = [int(number) for number in input().split()]
    first, second, third = values
    if first == second == third:
        return 10000 + first * 1000
    elif first != second and second != third and third != first:
        return max(values) * 100
    else:
        for val in values:
            if values.count(val) == 2:
                return 1000 + val * 100


if __name__ == "__main__":
    print(solution())
