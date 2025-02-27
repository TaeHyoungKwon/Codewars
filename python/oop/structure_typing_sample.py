from typing import Protocol, runtime_checkable


class PersonProtocol(Protocol):
    name: str
    age: int


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Employee:
    def __init__(self, name: str, height: int, department: str):
        self.name = name
        self.height = height
        self.department = department


def greet(person: PersonProtocol):
    print(f"Hello, {person.name}, age {person.height}")


employee = Employee("Alice", 30, "HR")
greet(employee)
