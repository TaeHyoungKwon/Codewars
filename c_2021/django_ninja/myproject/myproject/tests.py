import json

from django.test import Client, TestCase

BASE_URL = "http://127.0.0.1:8000"

client = Client()


def _call_api(url):
    response = client.get(url)
    return response.status_code, json.loads(response.content)


class TestDJNinjaWithPathParams(TestCase):
    def test_read_item_with_path_param(self):
        # Path parameters with types
        path_param = 3
        _, response = _call_api(url=f"{BASE_URL}/api/items/{path_param}")
        self.assertEqual(response["item_id"], 3)

    def test_read_item_on_data_validation_error_with_path_param(self):
        # Data validation
        path_param = "foo" # not int but str
        status_code, _ = _call_api(url=f"{BASE_URL}/api/items/{path_param}")
        self.assertEqual(status_code, 422)

    def test_events(self):
        # Multiple parameters
        year, month, day = 2021, 10, 11
        _, response = _call_api(url=f"{BASE_URL}/api/events/{year}/{month}/{day}")
        self.assertEqual(response["date"], [year, month, day])

    def test_events_with_schema(self):
        # Using Schema
        year, month, day = 2021, 10, 11
        _, response = _call_api(url=f"{BASE_URL}/api/events_with_schema/{year}/{month}/{day}")
        self.assertEqual(response["date"], "2021-10-11")


class TestDJNinjaWithQueryParams(TestCase):
    def test_list_weapons_query_param(self):
        # Query parameters
        limit = 10
        offset = 0
        _, response = _call_api(url=f"{BASE_URL}/api/weapons?offset={offset}&limit={limit}")
        self.assertEqual(response, ["Ninjato", "Shuriken", "Katana", "Kama", "Kunai", "Naginata", "Yari"])

    def test_list_weapons_query_param_with_schema(self):
        # Query parameters
        limit = 10
        offset = 0
        _, response = _call_api(url=f"{BASE_URL}/api/filter?offset={offset}&limit={limit}&query=abcde&categories=samplecate")
        self.assertEqual(response["filters"], {'limit': 10, 'offset': 0, 'query': 'abcde', 'category__in': ['samplecate']}
)
