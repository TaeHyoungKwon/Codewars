def solution():
    sanguen_number_count = int(input())
    sanguen_numbers = set(map(int, input().split()))
    target_number_count = int(input())
    target_numbers = map(int, input().split())
    return " ".join(str(int(target_number in sanguen_numbers)) for target_number in target_numbers)


if __name__ == "__main__":
    print(solution())
