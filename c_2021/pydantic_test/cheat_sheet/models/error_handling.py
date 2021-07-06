import json
from typing import List

from pydantic import ValidationError
from pydantic.main import BaseModel
from pydantic.types import conint


STR_E = """5 validation errors for Model
is_required
  field required (type=value_error.missing)
gt_int
  ensure this value is greater than 42 (type=value_error.number.not_gt; limit_value=42)
list_of_ints -> 2
  value is not a valid integer (type=type_error.integer)
a_float
  value is not a valid float (type=type_error.float)
recursive_model -> lng
  value is not a valid float (type=type_error.float)"""


ALL_ERROR_INFO = [
    {"loc": ("is_required",), "msg": "field required", "type": "value_error.missing"},
    {
        "loc": ("gt_int",),
        "msg": "ensure this value is greater than 42",
        "type": "value_error.number.not_gt",
        "ctx": {"limit_value": 42},
    },
    {"loc": ("list_of_ints", 2), "msg": "value is not a valid integer", "type": "type_error.integer"},
    {"loc": ("a_float",), "msg": "value is not a valid float", "type": "type_error.float"},
    {"loc": ("recursive_model", "lng"), "msg": "value is not a valid float", "type": "type_error.float"},
]


class Location(BaseModel):
    lat = 0.1
    lng = 10.1


class Model(BaseModel):
    is_required: float
    gt_int: conint(gt=42)
    list_of_ints: List[int] = None
    a_float: float = None
    recursive_model: Location = None


data = dict(
    list_of_ints=["1", 2, "bad"],
    a_float="not a float",
    recursive_model={"lat": 4.2, "lng": "New York"},
    gt_int=21,
)

if __name__ == "__main__":
    try:
        Model(**data)
    except ValidationError as e:
        pass

        assert e.errors() == ALL_ERROR_INFO  # 모든 error 관련 정보를 return 함
        assert isinstance(e.json(), str) is True  # 모든 error 관련 정보를 json으로 리턴
        assert str(e) == STR_E  # 사람이 읽기 좋은 형태로 error를 리턴해줌
        assert e.errors()[0]["loc"] == ("is_required",)
        assert e.errors()[0]["msg"] == "field required"
        assert e.errors()[0]["type"] == "value_error.missing"
