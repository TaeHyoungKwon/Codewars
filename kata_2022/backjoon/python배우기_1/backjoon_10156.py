def solution():
    snack_price, snack_count, remain_money = map(int, input().split())
    result = snack_price * snack_count - remain_money
    return result if result > 0 else 0


if __name__ == "__main__":
    print(solution())
