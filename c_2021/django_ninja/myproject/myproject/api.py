from ninja import NinjaAPI, Path

from myproject.schema import PathDate

api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return "Hello world"


@api.get("/items/{item_id}")
def read_item(request, item_id: int):
    """
    Path parameters with types, Data validation

    : item_id로는 int 만들어 올 수 있고, int 외 값이 들어오면, 422 status code를 발생 시킨다
    """
    return {"item_id": item_id}


@api.get("/events/{year}/{month}/{day}")
def events(request, year: int, month: int, day: int):
    """
    Multiple parameters
    """
    return {"date": [year, month, day]}


@api.get("/events_with_schema/{year}/{month}/{day}")
def events_with_schema(request, date: PathDate = Path(...)):
    """
    Using Schema

    * Path(...)은 Django ninjadprp 해당 스키마가 path param으로 적용된다는 것을 알려주는 용도
    """
    return {"date": date.value()}