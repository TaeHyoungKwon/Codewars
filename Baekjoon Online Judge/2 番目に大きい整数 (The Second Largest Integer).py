def solution(result):
    return sorted(result)[1]


if __name__ == "__main__":
    print(solution(map(int, input().split())))
