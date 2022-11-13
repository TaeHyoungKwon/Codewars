def solution():
    test_cases = int(input())

    result = []
    for _ in range(test_cases):
        x1, y1, x2, y2 = list(map(int, input().split()))
        planet_count = int(input())
        total_count = 0
        for _ in range(planet_count):
            cx, cy, cr = map(int, input().split())
            distance_1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
            distance_2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
            pow_cr = cr ** 2

            if pow_cr > distance_1 and pow_cr > distance_2:
                continue

            if pow_cr > distance_1 or pow_cr > distance_2:
                total_count += 1

        result.append(str(total_count))
    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
