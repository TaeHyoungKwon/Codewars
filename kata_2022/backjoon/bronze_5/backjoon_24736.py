def solution():
    result = []
    for _ in range(2):
        t, f, s, p, c = map(int, input().split())
        temp = t * 6 + f * 3 + s * 2
        if t and p:
            temp += p * 1
        if t and c:
            temp += c * 2

        result.append(temp)

    return f"{result[0]} {result[1]}"


if __name__ == "__main__":
    print(solution())
