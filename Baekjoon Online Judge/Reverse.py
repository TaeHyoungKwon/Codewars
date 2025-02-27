loop = int(input())

for i in range(loop):
    s, i, j = input().split()    
    i = int(i)
    j = int(j)

    print(s.replace(s[i:j], ""))

