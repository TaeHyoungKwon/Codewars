def solution():
    while True:
        try:
            n, s = map(int, input().split())
            print(s // (n + 1))
        except EOFError:
            break


if __name__ == "__main__":
    solution()
