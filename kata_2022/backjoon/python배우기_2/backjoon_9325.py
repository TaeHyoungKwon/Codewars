def solution():
    case_count = int(input())
    result = []
    for _ in range(case_count):
        car_price = int(input())
        option_count = int(input())

        if option_count == 0:
            result.append(car_price)
            continue

        temp = 0
        for _ in range(option_count):
            quantity, option_price = map(int, input().split())
            temp += quantity * option_price
        result.append(car_price + temp)

    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
