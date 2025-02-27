count = int(input())
numbers = list(map(int, input().split()))

is_happiness_score = sum(1 if number % 2 == 0 else -1 for number in numbers) > 0
if is_happiness_score:
    print("Happy")
else:
    print("Sad")
