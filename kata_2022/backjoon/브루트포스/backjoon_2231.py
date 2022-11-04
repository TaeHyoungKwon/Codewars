def solution():
    number = int(input())

    min_constructor = number
    for candidate_constructor in range(number)[::-1]:
        result = candidate_constructor + sum(int(digit) for digit in str(candidate_constructor))
        if result == number:
            min_constructor = candidate_constructor

    if min_constructor == number:
        return 0

    return min_constructor


if __name__ == "__main__":
    print(solution())
