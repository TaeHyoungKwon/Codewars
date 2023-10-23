import random
import string

from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        
    def __str__(self) -> str:
        return f"{self.name}, {self.address}"
    
    
@dataclass(slots=True)
class Person2:
    name: str
    address: str
    active: bool = True
    email_address: list[str] = field(default_factory=list)
    _id: str = field(init=False)
    _search_string: str = field(init=False)
    
    def __post_init__(self):
        self._id = generate_id()
        self._search_string = f"{self.name} {self.address}"


if __name__ == "__main__":
    person2 = Person2(name="John", address="123 Main St", active=False)
    print(person2)



