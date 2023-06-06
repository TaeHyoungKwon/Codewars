def solution(coins: list[int], target_price: int) -> int:
    total_count = 0

    for coin_price in sorted(coins, reverse=True):
        if target_price == 0:
            break

        if coin_price <= target_price:
            quotient, rest = divmod(target_price, coin_price)
            total_count += quotient
            target_price = rest

    return total_count


if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    print(solution(coins=coins, target_price=k))
