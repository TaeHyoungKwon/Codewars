max_value = 0
max_seminar = ""
for _ in range(7):
    input_value = input().split()
    seminar, count = input_value[0], int(input_value[1])
    if count > max_value:
        max_value = count
        max_seminar = seminar

print(max_seminar)
