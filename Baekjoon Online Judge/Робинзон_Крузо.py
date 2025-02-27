def solution(num):
    return "V" * (num // 5) + "I" * (num % 5)


num = int(input())
print(solution(num))
