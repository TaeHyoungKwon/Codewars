def diamond(n):
    if n > 0 and n % 2:
        return '\n'.join(' ' * ((n-i)//2) + '*' * i for i in range(1, n, 2) + range(n, 0, -2)) + '\n'
