#!/usr/bin/python3
# test cases for base class
import unittest
from models.base_model import BaseModel
from models.user import User
import models.base_model
import models.user
import inspect
import datetime
from time import sleep


class TestUser(unittest.TestCase):

    def setUp(self):

        self.c = User()

    def test_doc_user(self):

        self.assertIsNotNone(User.__doc__, 'no docs for Base class')
        self.assertIsNotNone(models.user.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(User, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_init_user(self):

        self.assertEqual(type(self.c.id), str)
        self.assertEqual(type(self.c.updated_at), datetime.datetime)
        self.assertEqual(type(self.c.created_at), datetime.datetime)

    def test_save_user(self):

        current_updatedAt = self.c.updated_at
        self.c.save()
        self.assertNotEqual(current_updatedAt, self.c.updated_at)

        with self.assertRaises(TypeError):
            self.c.save(13)

    def test_to_dict_city(self):

        self.c.first_name = "jonas"
        self.c.last_name = "stones"
        self.c.email = "jonas@example.com"
        self.c.password = "root"
        dict1 = self.c.to_dict()

        self.assertEqual(type(dict1['first_name']), str)
        self.assertEqual(dict1['first_name'], "jonas")
        self.assertEqual(dict1['last_name'], "stones")
        self.assertEqual(dict1['email'], "jonas@example.com")
        self.assertEqual(dict1['password'], "root")
        self.assertEqual(type(dict1['__class__']), str)
        self.assertEqual(dict1['__class__'], "User")
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['id']), str)
        self.assertEqual(type(dict1['created_at']), str)

        with self.assertRaises(TypeError):
            self.c.to_dict('str')


if __name__ == '__main__':
    unittest.main()