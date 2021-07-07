from pydantic import BaseModel, ValidationError, validator


class Model(BaseModel):
    foo: str

    @validator("foo")
    def name_must_contain_space(cls, v):
        if v != "bar":
            raise ValueError('value must be "bar"')

        return v


if __name__ == "__main__":
    try:
        Model(foo="ber")
    except ValidationError as e:
        print(e.errors())
        assert e.errors()[0]["loc"][0] == "foo"
        assert e.errors()[0]["msg"] == 'value must be "bar"'
        assert e.errors()[0]["type"] == "value_error"
        """
        [
            {
                'loc': ('foo',),
                'msg': 'value must be "bar"',
                'type': 'value_error',
            },
        ]
        """
