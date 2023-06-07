def solution(m: int, k: int, target_list: list[int]) -> int:
    first, second = sorted(target_list, reverse=True)[:2]

    temp = 0
    count = 0
    for i in range(m):

        if count == k:
            temp += second
            count = 0
            continue

        temp += first
        count += 1

    return temp


if __name__ == "__main__":
    _, m, k = map(int, input().split())
    target_list = [int(ele) for ele in input().split()]
    print(solution(m, k, target_list))


"""

5 7 2
3 4 3 4 3

5 8 3
2 4 5 4 6

"""