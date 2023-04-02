def solution(x: int, l: int, r: int):
    result = {abs(x - ele): ele for ele in range(l, r + 1)}
    return min(result.items(), key=lambda x: x[0])[1]


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
