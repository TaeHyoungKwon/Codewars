from collections import Counter


def main(socks: list[int]):
    return next(sock for sock, num in Counter(socks).items() if num % 2 == 1)


if __name__ == "__main__":
    print(main(socks=[int(input()) for _ in range(5)]))
