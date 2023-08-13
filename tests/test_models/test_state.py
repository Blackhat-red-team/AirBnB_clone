#!/usr/bin/python3
# test cases for base class
import unittest
from models.base_model import BaseModel
from models.state import State
import models.base_model
import models.state
import inspect
import datetime
from time import sleep


class TestState(unittest.TestCase):

    def setUp(self):

        self.s = State()

    def test_doc_state(self):

        self.assertIsNotNone(models.state.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(State, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_init_state(self):

        self.assertEqual(type(self.s.id), str)
        self.assertEqual(type(self.s.updated_at), datetime.datetime)
        self.assertEqual(type(self.s.created_at), datetime.datetime)

    def test_save_state(self):

        current_updatedAt = self.s.updated_at
        self.s.save()
        self.assertNotEqual(current_updatedAt, self.s.updated_at)

        with self.assertRaises(TypeError):
            self.s.save(13)

    def test_to_dict_state(self):

        self.s.name = "NYC"
        dict1 = self.s.to_dict()

        self.assertEqual(type(dict1['name']), str)
        self.assertEqual(type(dict1['__class__']), str)
        self.assertEqual(dict1['__class__'], "State")
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['id']), str)
        self.assertEqual(type(dict1['created_at']), str)

        with self.assertRaises(TypeError):
            self.s.to_dict('str')


if __name__ == '__main__':
    unittest.main()
