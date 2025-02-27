def solution(a: int, b: int, x: int) -> int:
    return a * (x - 1) + b


loop = int(input())
for _ in range(loop):
    a, b, x = list(map(int, input().split()))
    print(solution(a, b, x))
