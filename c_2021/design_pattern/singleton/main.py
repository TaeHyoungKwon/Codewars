import unittest
import sqlite3


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def __init__(self):
        self.cursor_obj = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursor_obj = self.connection.cursor()
        return self.cursor_obj


class TestDBSingleton(unittest.TestCase):
    def test_db_singleton(self):
        db1 = Database().connect()
        db2 = Database().connect()
        self.assertEqual(db1, db2)
