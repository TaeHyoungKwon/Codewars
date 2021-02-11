def f1(x):
    return x * 2


def f2(x):
    return x + 2


def f3(x):
    return x ** 2


def chained(functions):
    def apply(param):
        result = param
        for f in functions:
            result = f(result)
        return result

    return apply


if __name__ == "__main__":
    print(chained([f1, f2, f3])(1))
