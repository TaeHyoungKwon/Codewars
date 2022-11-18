def solution():
    expected_total = int(input())
    loop = int(input())

    total = 0
    for _ in range(loop):
        price, quantity = map(int, input().split())
        total += price * quantity

    return "Yes" if total == expected_total else "No"


if __name__ == "__main__":
    print(solution())
