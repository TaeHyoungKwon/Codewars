def solution():
    """아직못품"""
    n = int(input())
    prev_number_1 = 1
    prev_number_2 = 1
    for i in range(1, n + 1):
        candidate_1 = 8 * i - 7
        candidate_2 = 8 * i - 3

        if candidate_1 == n:
            return 1

        if candidate_2 == n:
            return 5

        if candidate_1 < n and candidate_2 < n:
            prev_number_1 = candidate_1
            prev_number_2 = candidate_2
            continue

        if n - prev_number_1 < n - prev_number_2:
            return




        if first_number > n:
            if n - prev_number + 1 <= 5:
                return n - prev_number + 1
            else:
                return n - prev_number + 1



if __name__ == "__main__":
    print(solution())
