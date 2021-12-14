from ninja import NinjaAPI, Path, Query

from myproject.schema import Filters, PathDate

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


WEAPONS = ["Ninjato", "Shuriken", "Katana", "Kama", "Kunai", "Naginata", "Yari"]


@api.get("/weapons")
def list_weapons(request, limit: int = 10, offset: int = 0):
    """
    Query param

    * path param이 아닌, 함수 param은 query param으로 본다
    * path param과 마찬가지로, parsing, validation, 자동 문서화 등에 장점을 가진다
    * limit과 offset의 type은 함수 내부에서는 str로 변경된
    """
    return WEAPONS[offset: offset + limit]


@api.get("/filter")
def events(request, filters: Filters = Query(...)):
    """
    Query Param (Using Schema)

    filters.dict()
    --> ex) {'limit': 10, 'offset': 0, 'query': 'abcde', 'category__in': ['samplecate']}

    """
    return {"filters": filters.dict()}


@api.get("/items/test/{int:item_id}")
def read_item_with_path_converter(request, item_id):
    return {"item_id": item_id}



