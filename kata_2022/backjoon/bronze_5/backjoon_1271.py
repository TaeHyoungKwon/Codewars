def solution():
    m, n = map(int, input().split())
    q, r = divmod(m, n)
    return f"{q}\n{r}"


if __name__ == "__main__":
    print(solution())
