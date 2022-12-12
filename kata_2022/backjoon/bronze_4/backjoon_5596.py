def solution():
    mingook_total_sum = sum(map(int, input().split()))
    manse_total_sum = sum(map(int, input().split()))

    if mingook_total_sum == manse_total_sum:
        return mingook_total_sum
    else:
        return max([mingook_total_sum, manse_total_sum])


if __name__ == "__main__":
    print(solution())
