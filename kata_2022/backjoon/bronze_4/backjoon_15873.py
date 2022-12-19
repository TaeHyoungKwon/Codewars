def solution(number: int) -> int:
    last_two_digits = int(str(number)[-2:])
    if last_two_digits == 10:
        return int(str(number)[:-2]) + last_two_digits
    else:
        return int(str(number)[:-1]) + int(str(number)[-1])


if __name__ == "__main__":
    number = int(input())
    print(solution(number))
