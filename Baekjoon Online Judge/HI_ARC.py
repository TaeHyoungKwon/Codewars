def solution(h: int, i: int, a: int, r: int, c: int) -> int:
    return h * i - a * r * c


h, i, a, r, c = list(map(int, input().split()))
print(solution(h, i, a, r, c))
