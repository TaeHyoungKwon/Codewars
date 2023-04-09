def solution(stamp_count: int, price: int) -> int:
    discount_cases = []
    if stamp_count < 5:
        discount_cases.append(price)
    if stamp_count >= 5:
        discount_cases.append(price - 500)
    if stamp_count >= 10:
        discount_cases.append(price - (price * 0.1))
    if stamp_count >= 15:
        discount_cases.append(price - 2000)
    if stamp_count >= 20:
        discount_cases.append(price - (price * 0.25))

    minimum_discount_price = min(discount_cases)
    if minimum_discount_price < 0:
        return 0
    return int(minimum_discount_price)


if __name__ == "__main__":
    print(solution(stamp_count=int(input()), price=int(input())))
