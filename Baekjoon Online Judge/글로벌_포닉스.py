s1 = input()
s2 = input()
s3 = input()

FOR_GLOBAL = {"l", "k", "p"}

condition_1 = s1[0] in FOR_GLOBAL and s2[0] in FOR_GLOBAL and s3[0] in FOR_GLOBAL
condition_2 = set(f"{s1[0]}{s2[0]}{s3[0]}") == set(FOR_GLOBAL)

if condition_1 and condition_2:
    print("GLOBAL")
else:
    print("PONIX")
