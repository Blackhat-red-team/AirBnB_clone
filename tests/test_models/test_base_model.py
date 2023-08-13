#!/usr/bin/python3
"""Unittest for base model"""
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import models.base_model
import inspect
import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """This method is called before each test method in the test class."""
        self.z = BaseModel()

    def test_doc(self):
        """test_doc(self): to test if module and class have docs"""
        self.assertIsNotNone(BaseModel.__doc__, 'no docs for Base class')
        self.assertIsNotNone(models.base_model.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(BaseModel, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_save(self):
        """test save class method"""
        before_update_time = self.z.updated_at
        self.z.my_number = 90
        self.z.save()
        after_update_time = self.z.updated_at
        all_objects = storage.all()
        object_key = "{}.{}".format(self.z.__class__.__name__, self.z.id)
        saved_object = all_objects[object_key]
        new_number = saved_object.my_number
        self.assertNotEqual(before_update_time, after_update_time)
        self.assertEqual(new_number, 90)




    def test_model_from_dict(self):
        """test instantiation from a dictionary"""
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

    def test_to_dict(self):
        """test BaseModel.to_dict()"""
        self.z.name = "My First Model"
        self.z.my_number = 89
        vmdict1 = self.z.to_dict()
        self.assertEqual(type(vmdict1['my_number']), int)
        self.assertEqual(type(vmdict1['name']), str)
        self.assertEqual(type(vmdict1['__class__']), str)
        self.assertEqual(vmdict1['__class__'], 'BaseModel')
        self.assertEqual(type(vmdict1['updated_at']), str)
        self.assertEqual(type(vmdict1['id']), str)
        self.assertEqual(type(vmdict1['created_at']), str)

    def test_init_with_invalid_dates(self):
        """Test initialization with invalid date strings"""
        invaldd_dict = {
            'id': '123',
            'created_at': '2021-08-07T15:30:51.120690',
            'updated_at': '2023-08-07T15:30:51.120690',
            'name': 'julien',
            'my_number': 42
        }
        invaldd_dict['created_at'] = "INVALID DATE"
        with self.assertRaises(ValueError):
            inst = BaseModel(**invaldd_dict)

        invaldd_dict['updated_at'] = "2023"  # Set invalid updated at
        with self.assertRaises(ValueError):
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
        news_inst = BaseModel()  # create sleep update
        beforeSaved_updated_at = news_inst.updated_at
        news_inst.save()
        self.assertLess(beforeSaved_updated_at, news_inst.updated_at)


if __name__ == '__main__':
    unittest.main()
