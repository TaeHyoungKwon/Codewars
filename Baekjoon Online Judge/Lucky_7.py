def solution(num):
    if "7" in num and int(num) % 7 == 0:
        return 3
    elif "7" in num and int(num) % 7 != 0:
        return 2
    elif "7" not in num and int(num) % 7 == 0:
        return 1
    else:
        return 0


print(solution(input()))
