import unittest


def capital(capitals):
    temp = []
    for ele in capitals:
        if ele.get("state"):
            first = ele["state"]
        elif ele.get("country"):
            first = ele["country"]
        second = ele["capital"]
        completed = f"The capital of {first} is {second}"
        temp.append(completed)
    return temp

# def capital(capitals):
#     return [f"The capital of {c.get('state') or c['country']} is {c['capital']}" for c in capitals]

class TestCapital(unittest.TestCase):
    def test_capital_with_one_element(self):
        self.assertEqual(
            capital(capitals=[{"state": "Maine", "capital": "Augusta"}]), ["The capital of Maine is Augusta"]
        )

    def test_capital_with_two_element(self):
        self.assertEqual(
            capital(capitals=[{"state": "Maine", "capital": "Augusta"}, {"country": "Korea", "capital": "Seoul"}]),
            ["The capital of Maine is Augusta", "The capital of Korea is Seoul"],
        )
