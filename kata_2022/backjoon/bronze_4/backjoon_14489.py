def solution(balance_a: int, balance_b: int, chicken_price: int) -> int:
    sum_of_balances = balance_a + balance_b

    return (
        sum_of_balances
        if sum_of_balances < (chicken_price * 2)
        else sum_of_balances - (chicken_price * 2)
    )


if __name__ == "__main__":
    balance_a, balance_B = map(int, input().split())
    chicken_price = int(input())
    print(solution(balance_a, balance_B, chicken_price))
