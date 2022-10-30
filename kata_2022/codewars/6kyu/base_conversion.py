bin = '01'
oct = '01234567'
dec = '0123456789'
hex = '0123456789abcdef'
allow = 'abcdefghijklmnopqrstuvwxyz'
allup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert(input, source, target):
    n = sum(source.find(d) * (len(source) ** i) for i, d in enumerate(input[::-1]))
    result = []
    while n:
        n, r = divmod(n, len(target))
        result.insert(0, target[r])
    return ''.join(result or [target[0]])


class TestConvert:
    def test_convert(self):
        assert convert("15", dec, bin) == "1111"
