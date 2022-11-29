def solution():
    case_count = int(input())

    result = []
    for _ in range(case_count):
        numbers = sorted(list(map(int, input().split())), reverse=True)
        except_min_n_max = numbers[1:-1]
        if max(except_min_n_max) - min(except_min_n_max) >= 4:
            result.append("KIN")
        else:
            result.append(sum(except_min_n_max))

    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
