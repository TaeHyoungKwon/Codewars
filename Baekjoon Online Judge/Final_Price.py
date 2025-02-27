n = int(input())
initial_price = int(input())
price_variations = [int(input()) for _ in range(n - 1)]

print(initial_price + sum(price_variations))
