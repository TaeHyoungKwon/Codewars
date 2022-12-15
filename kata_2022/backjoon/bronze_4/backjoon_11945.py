def solution():
    n, m = map(int, input().split())
    return "\n".join("".join(input().split())[::-1] for _ in range(n))


if __name__ == "__main__":
    print(solution())
