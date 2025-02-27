n = int(input())
menu_prices = [int(input()) for _ in range(n)]
m = int(input())
corner_numbers = [int(input()) for _ in range(m)]

print(sum(menu_prices[corner_number - 1] for corner_number in corner_numbers))
