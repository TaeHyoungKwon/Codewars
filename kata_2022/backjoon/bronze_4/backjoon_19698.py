def solution(n: int, w: int, h: int, l: int) -> int:
    w = w // l
    h = h // l
    result = w * h
    return n if result > n else result


if __name__ == "__main__":
    n, w, h, l = map(int, input().split())
    print(solution(n, w, h, l))
