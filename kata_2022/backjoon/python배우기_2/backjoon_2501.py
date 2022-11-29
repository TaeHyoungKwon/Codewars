def solution():
    target_number, index_ = map(int, input().split())
    try:
        result = [
            candidate_number
            for candidate_number in range(1, target_number + 1)
            if target_number % candidate_number == 0
        ][index_ - 1]
    except IndexError:
        result = 0

    return result



if __name__ == "__main__":
    print(solution())
