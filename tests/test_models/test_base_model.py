#!/usr/bin/python3
"""Unittest for base model"""
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import models.base_model
import inspect
import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    def setUpz(self):
        """This method is called before each test method in the test class.
        """
        self.z = BaseModel()

    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(BaseModel.__doc__, 'no docs for Base class')
        self.assertIsNotNone(models.base_model.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(BaseModel, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_save(self):
        """"
            test save class method
        """
        before_update_time = self.base.updated_at
        self.base.my_number = 90
        self.base.save()
        after_update_time = self.base.updated_at
        self.assertNotEqual(before_update_time, after_update_time)
        all_objects = storage.all()
        new_number = all_objects[self.base.__class__.__name__ +
                                 "." + self.base.id]["my_number"]
        self.assertEqual(new_number, 90)

    def test_model_from_dict(self):
        """test instantiation from a dictionary
        """
        # Example dictionary with attribute values
        instad_dic = {
            '__class__': "BaseModel",
            'id': '123',
            'created_at': '2023-08-07T15:30:51.120683',
            'updated_at': '2023-08-07T15:30:51.120690',
            'name': 'julien',
            'my_number': 42
        }
        test_instad = BaseModel(**instad_dic)
        self.assertNotIn("__class__", test_instad.__dict__)
        self.assertEqual(type(test_instad.id), str)
        self.assertEqual(type(test_instad.created_at), datetime.datetime)
        self.assertEqual(type(test_instad.updated_at), datetime.datetime)
        self.assertEqual(type(test_instad.name), str)
        self.assertEqual(type(test_instad.my_number), int)

    def test_to_dozt(self):
        """ test BaseModel.to_dict() """
        self.z.name = "My First Model"
        self.z.my_number = 89
        vmdict1 = self.z.to_dict()

    def test_to_doet(self):
        """ test BaseModel.to_dict() """
        self.z.name = "My First Model"
        self.z.my_number = 89
        vmdict1 = self.z.to_dict()

        """ confirming the type of each attr in dict """
        self.assertEqual(type(vmdict1['my_number']), int)
        self.assertEqual(type(vmdict1['name']), str)
        self.assertEqual(type(vmdict1['__class__']), str)
        self.assertEqual(vmdict1['__class__'], 'BaseModel')
        self.assertEqual(type(vmdict1['updated_at']), str)
        self.assertEqual(type(vmdict1['id']), str)
        self.assertEqual(type(vmdict1['created_at']), str)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.z.to_dict('str')

        """ confirming the type of each attr in dict """
        self.assertEqual(type(vmdict1['my_number']), int)
        self.assertEqual(type(vmdict1['name']), str)
        self.assertEqual(type(vmdict1['__class__']), str)
        self.assertEqual(vmdict1['__class__'], 'BaseModel')
        self.assertEqual(type(vmdict1['updated_at']), str)
        self.assertEqual(type(vmdict1['id']), str)
        self.assertEqual(type(vmdict1['created_at']), str)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.z.to_dict('str')

        """Unittests for task 4
        """
    def init_with_invaidd_dates(self):
        """Test initialization with invalid date strings
        """
        # Example dictionary with attribute values
        invaldd_dict = {
            'id': '123',
            'created_at': '2021-08-07T15:30:51.120690',
            'updated_at': '2023-08-07T15:30:51.120690',
            'name': 'julien',
            'my_number': 42
        }
        # Set invalid date string for created_at
        invaldd_dict['created_at'] = "INVALID DATE"
        with self.assertRaises(ValueError):
            inst = BaseModel(**invaldd_dict)

        # set invalid updated at:
        invaldd_dict['updated_at'] = 2023
        with self.assertRaises(TypeError):
            inst = BaseModel(**invaldd_dict)

    def test_str(self):
        """Testing __str__ method"""
        self.z.id = "1234"
        strForm = self.z.__str__()
        expected = "[BaseModel] (1234)"
        self.assertIn(expected, strForm)

    def test_saved_updatedAt(self):
        """test updating the public instance attribute updated_at
            with the current datetime"""
        news_inzt = BaseModel()  # create sleep update
        sleep(0.05)
        beforeSaved_updated_at = news_inzt.updated_at
        news_inzt.save()
        self.assertLess(beforeSaved_updated_at, news_inzt.updated_at)


if __name__ == '__main__':
    unittest.main()
