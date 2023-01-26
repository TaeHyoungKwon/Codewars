def solution(tea_type: int, answer: list[int]):
    return answer.count(tea_type)


if __name__ == "__main__":
    tea_type = int(input())
    answer = [int(ele) for ele in input().split()]
    print(solution(tea_type, answer))
