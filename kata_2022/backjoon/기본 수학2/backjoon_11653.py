def solution():
    number = int(input())

    prime_numbers = [i for i in range(1, number + 1) if _is_prime(i)]

    for prime_number in prime_numbers:
        # 여기부터
        while True:
            print(prime_number)
            q, r = divmod(number, prime_number)
            if q == 1:
                break

            if r == 0:
                number = q
        if q == 1:
            return


def _is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(solution())
