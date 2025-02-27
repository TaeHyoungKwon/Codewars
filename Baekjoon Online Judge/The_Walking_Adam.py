case = int(input())

for _ in range(case):
    trials = input()
    
    count = 0
    for trial in trials:
        if trial == "D":
            break
        count += 1
        
    print(count)