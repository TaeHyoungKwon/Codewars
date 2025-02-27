def solution(w: int, h: int) -> str:
    return f"{w * h / 2:.1f}"


w, h = list(map(int, input().split()))
print(solution(w, h))
