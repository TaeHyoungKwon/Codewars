from pydantic import BaseModel, ValidationError, validator, PydanticValueError


class NotABarError(PydanticValueError):
    code = "not_a_bar"
    msg_template = "value is not 'bar', got '{wrong_value}'"


class Model(BaseModel):
    foo: str

    @validator("foo")
    def name_must_contain_space(cls, v):
        if v != "bar":
            raise NotABarError(wrong_value=v)
        return v


if __name__ == "__main__":
    try:
        Model(foo="ber")
    except ValidationError as e:
        # print(e.json())
        print(e.errors()[0]["msg"])
        assert e.errors()[0]["loc"][0] == "foo"
        assert e.errors()[0]["msg"] == "value is not 'bar', got 'ber'"
        assert e.errors()[0]["type"] == "value_error.not_a_bar"
        assert e.errors()[0]["ctx"]["wrong_value"] == "ber"
        """
        [
          {
            "loc": [
              "foo"
            ],
            "msg": "value is not \"bar\", got \"ber\"",
            "type": "value_error.not_a_bar",
            "ctx": {
              "wrong_value": "ber"
            }
          }
        ]
        """
