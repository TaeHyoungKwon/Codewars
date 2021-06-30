import json

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "Jane Doe"


user = User(id="123")

if __name__ == "__main__":
    assert user.id == 123
    assert user.name == "Jane Doe"
    assert user.dict() == dict(user) == {"id": 123, "name": "Jane Doe"}
    assert user.json() == json.dumps(user.dict())
    assert user.copy() == user
    assert user.copy().id == user.id  # shallow copy
    assert User.parse_obj({"id": 123, "name": "Jane Doe"}) == user
    assert User.parse_raw(user.json()) == user
