def solution(number):
    return f"{number}. {input()}"


if __name__ == "__main__":
    case_count = int(input())
    for index_ in range(1, case_count + 1):
        print(solution(index_))
