from math import ceil


def solution(n: int, a: int, b: int, c: int, d: int) -> int:
    def _calculate(total_buying_count: int, buying_count: int, price: int) -> int:
        return ceil(total_buying_count / buying_count) * price

    return min(_calculate(n, a, b), _calculate(n, c, d))


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
