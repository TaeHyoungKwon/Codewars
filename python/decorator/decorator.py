from typing import Callable

# python function
def hello_world(name: str) -> str:
    return f"Hello World {name}"


# first-class objects
def say_hello(name: str) -> str:
    return f"Hello {name}"


def be_awsome(name: str) -> str:
    return f"Yo {name}, together we are the awesome!"


def greet_bob(greeter_func: Callable) -> str:
    return greeter_func("Bob")

if __name__ == "__main__":
    print(greet_bob(hello_world))

