from collections import Counter


def solution():
    # 다 못품`
    case_count = int(input())
    numbers = []
    for _ in range(case_count):
        numbers.append(int(input()))

    print(round(sum(numbers) / len(numbers)))
    print(sorted(numbers)[case_count // 2])
    cnt_result = Counter(numbers).most_common()
    if len(numbers) > 1:
        if cnt_result[0][1] == cnt_result[1][1]:
            return cnt_result[1][0]
    print(Counter(numbers).most_common())
    print(max(numbers) - min(numbers))


if __name__ == "__main__":
    solution()
