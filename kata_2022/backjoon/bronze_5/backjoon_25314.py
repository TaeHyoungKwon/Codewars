def solution():
    n = int(input())
    result = ["long" for _ in range(n // 4)]
    result.append("int")
    return " ".join(result)


if __name__ == "__main__":
    print(solution())
