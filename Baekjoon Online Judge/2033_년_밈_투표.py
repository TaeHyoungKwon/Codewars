PROMISES = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
]

loop = int(input())
if all(input() in PROMISES for _ in range(loop)):
    print("No")
else:
    print("Yes")
