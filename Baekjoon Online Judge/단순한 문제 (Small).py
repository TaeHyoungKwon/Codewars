# https://movegreen.tistory.com/48

def solution(numbers: list[int]) -> int:
    return min(numbers)


if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        print(solution([int(ele) for ele in input().split()]))
