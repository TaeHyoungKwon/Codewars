retrial_subject_code = input()
available_subject_count = int(input())


count = 0
for _ in range(available_subject_count):
    input_subject_code = input()
    target = retrial_subject_code[:5]
    if input_subject_code[:5] == target:
        count += 1

print(count)

