def hanoi(n: int, src: int, dst: int):
    if n == 0:
        return
    via = 6 - src - dst
    hanoi(n - 1, src, via)
    print(src, dst)
    hanoi(n - 1, via, dst)


if __name__ == "__main__":
    n = int(input())
    print(2**n - 1)
    if n <= 20:
        hanoi(n, 1, 3)
