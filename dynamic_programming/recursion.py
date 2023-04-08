def sum_of_numbers(n: int) -> int:
    return sum(i for i in range(1, n + 1))


def sum_of_numbers_for_recursion(n: int) -> int:
    if n == 1:
        return 1
    return sum_of_numbers_for_recursion(n - 1) + n


def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_for_recursion(n: int) -> int:
    if n == 1:
        return 1
    return factorial_for_recursion(n - 1) * n


def accumulate(numbers: list[int], i: int) -> list[int]:
    if i == len(numbers):
        return numbers

    numbers[i] += numbers[i - 1]
    return accumulate(numbers, i + 1)


def sqrt_recursive(n: int) -> int:
    if n == 1:
        return n

    return sqrt_recursive(n - 1) ** n


if __name__ == "__main__":
    #assert sum_of_numbers(5) == 15
    #assert sum_of_numbers_for_recursion(5) == 15

    #assert factorial(5) == 120
    #assert factorial_for_recursion(5) == 120

    assert accumulate(numbers=[1, 2, 3, 4, 5], i=1) == [1, 3, 6, 10, 15]
