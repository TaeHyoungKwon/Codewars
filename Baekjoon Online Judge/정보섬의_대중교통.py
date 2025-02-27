def solution(a: int, b: int) -> str:
    if a < b:
        return "Bus"
    elif a > b:
        return "Subway"
    else:
        return "Anything"


_, a, b = list(map(int, input().split()))
print(solution(a, b))
