import sys

maps = {
    "CU": "see you",
    ":-)": "I’m happy",
    ":(": "I’m unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
    "(~.~)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you’re welcome",
    "TTYL": "talk to you later",
}


for short_form in sys.stdin:
    result = short_form.strip()
    print(maps.get(result, result))
