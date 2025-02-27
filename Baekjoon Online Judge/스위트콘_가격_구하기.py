VAT = 0.1


def solution(b: int) -> int:
    return round(b / (1 + VAT))


b = int(input())
print(solution(b))
