def solution(n: int, m: int, k: int) -> int:
    front = m * ["O"] + (n - m) * ["X"]
    back = k * ["O"] + (n - k) * ["X"]
    return sum(1 for f_ele, b_ele in zip(front, back) if f_ele == b_ele)


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    print(solution(n, m, k))
