t = int(input())
standard_score = list(map(int, input().split()))+ [0] * (5 - t)

result = 0
if standard_score[0] > standard_score[2]:
    result += (standard_score[0] - standard_score[2]) * 508
else:
    result += (standard_score[2] - standard_score[0]) * 108

if standard_score[1] > standard_score[3]:
    result += standard_score[1] - standard_score[3] * 212
else:
    result += abs(standard_score[1] - standard_score[3]) * 305

if standard_score[4] > 0:
    result += standard_score[4] * 707

print(result * 4763)