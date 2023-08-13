#!/usr/bin/python3
""" test console """
import unittest
import inspect
from console import HBNBCommand
import console
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json


class TestConsole(unittest.TestCase):
   

    def test_doicz_console(self):
      
        self.assertIsNotNone(HBNBCommand.__doc__, 'no docs for Base class')
        self.assertIsNotNone(console.__doc__, 'no docs for module')

    def test_quii_EOF(self):
        
        self.assertEqual(HBNBCommand().onecmd("EOF"), True)
        self.assertEqual(HBNBCommand().onecmd("quit"), True)

    def test_emp_linn(self):
        
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertEqual("", output.getvalue())


class TestCreate(unittest.TestCase):
   

    def test_arg_leng(self):
        
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = "create"
            expected = "** class name missing **"
            HBNBCommand().onecmd(inppt)
            self.assertEqual(expected, output.getvalue().strip())

    def test_inva_classNam(self):
        
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = "create UnknownClass"
            expected = "** class doesn't exist **"
            HBNBCommand().onecmd(inppt)  # excute command
            self.assertEqual(expected, output.getvalue().strip())

    def test_creited(self):
        
        
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = "create BaseModel"  # inppt
            HBNBCommand().onecmd(inppt)  # excute command
            captorrz_id = output.getvalue().strip()

            innst_key = "BaseModel.{}".format(captorrz_id)
            inppt = "create BaseModel"
            self.assertIn(innst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = "create User"  # inppt
            HBNBCommand().onecmd(inppt)  # excute command
            captorrz_id = output.getvalue().strip()

            innst_key = "User.{}".format(captorrz_id)
            inppt = "create User"
            self.assertIn(innst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = "create Amenity"  # inppt
            HBNBCommand().onecmd(inppt)  # excute command
            captorrz_id = output.getvalue().strip()

            innst_key = "Amenity.{}".format(captorrz_id)
            inppt = "create Amenity"
            self.assertIn(innst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = "create State"  # inppt
            HBNBCommand().onecmd(inppt)  # excute command
            captorrz_id = output.getvalue().strip()

            innst_key = "State.{}".format(captorrz_id)
            inppt = "create State"
            self.assertIn(innst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = "create Place"  # inppt
            HBNBCommand().onecmd(inppt)  # excute command
            captorrz_id = output.getvalue().strip()

            innst_key = "Place.{}".format(captorrz_id)
            inppt = "create Place"
            self.assertIn(innst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = "create City"  # inppt
            HBNBCommand().onecmd(inppt)  # excute command
            captorrz_id = output.getvalue().strip()

            innst_key = "City.{}".format(captorrz_id)
            inppt = "create City"
            self.assertIn(innst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = "create Review"  # inppt
            HBNBCommand().onecmd(inppt)  # excute command
            captorrz_id = output.getvalue().strip()

            innst_key = "Review.{}".format(captorrz_id)
            self.assertIn(innst_key, storage.all().keys())


class TestShwwd(unittest.TestCase):

    def test_show(self):
        
        z = BaseModel()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'BaseModel.show("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            res = f"[BaseModel] ({id}) {z.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        z = User()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'User.show("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            res = f"[User] ({id}) {z.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        z = State()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'State.show("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            res = f"[State] ({id}) {z.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        z = City()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'City.show("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            res = f"[City] ({id}) {z.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        z = Place()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'Place.show("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            res = f"[Place] ({id}) {z.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        z = Amenity()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'Amenity.show("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            res = f"[Amenity] ({id}) {z.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        z = Review()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'Review.show("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            res = f"[Review] ({id}) {z.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

    def test_errors(self):
        
        invalid_id = 23421123
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'BaseModel.show("{invalid_id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            res = "** no instance found **"
            self.assertEqual(output.getvalue().strip(), res)

     
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'show'
            HBNBCommand().onecmd(inppt)  # excute command
            res = "** class name missing **"
            self.assertEqual(output.getvalue().strip(), res)

        
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'places.show("232342")'
            HBNBCommand().onecmd(inppt)  # excute command
            res = "** class doesn't exist **"
            self.assertEqual(output.getvalue().strip(), res)

        
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'Place.show()'
            HBNBCommand().onecmd(inppt)  # excute command
            res = "** instance id missing **"
            self.assertEqual(output.getvalue().strip(), res)


class TestCount(unittest.TestCase):
    
    def test_count(self):
        """ test count function """
        count = 0
        for key, values in storage.all().items():
            name = key.split(".")
            if name[0] == 'BaseModel':
                count += 1
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'BaseModel.count()'
            HBNBCommand().onecmd(inppt)
            self.assertEqual(output.getvalue().strip(), str(count))


class TestAll(unittest.TestCase):
    
    def test_all(self):
        
        z = BaseModel()
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'BaseModel.all()'
            HBNBCommand().onecmd(inppt)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[BaseModel]")

        z = User()
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'User.all()'
            HBNBCommand().onecmd(inppt)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[User]")

        z = State()
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'State.all()'
            HBNBCommand().onecmd(inppt)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[State]")

        z = City()
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'City.all()'
            HBNBCommand().onecmd(inppt)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[City]")

        z = Amenity()
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'Amenity.all()'
            HBNBCommand().onecmd(inppt)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[Amenity]")

        z = Place()
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'Place.all()'
            HBNBCommand().onecmd(inppt)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[Place]")

        z = Review()
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'Review.all()'
            HBNBCommand().onecmd(inppt)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[Review]")

    def test_invalidClass(self):
        
        z = Review()
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'review.all()'
            HBNBCommand().onecmd(inppt)
            expected_output = "** class doesn't exist **"
            self.assertEqual(output.getvalue().strip(), expected_output)


class TestDestroy(unittest.TestCase):
    
    def test_invalidId(self):
       
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'BaseModel.destroy("232342")'
            HBNBCommand().onecmd(inppt)  # excute command
            res = "** no instance found **"
            self.assertEqual(output.getvalue().strip(), res)

    def test_destroy(self):
     
        z = BaseModel()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'BaseModel.destroy("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            instances = storage.all()
            list_keys = []
            for key, obj in instances.items():
                list_keys.append(key)
            self.assertNotIn(id, list_keys)

        z = User()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'User.destroy("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            instances = storage.all()
            list_keys = []
            for key, obj in instances.items():
                list_keys.append(key)
            self.assertNotIn(id, list_keys)

        z = State()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'State.destroy("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            instances = storage.all()
            list_keys = []
            for key, obj in instances.items():
                list_keys.append(key)
            self.assertNotIn(id, list_keys)

        z = City()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'City.destroy("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            instances = storage.all()
            list_keys = []
            for key, obj in instances.items():
                list_keys.append(key)
            self.assertNotIn(id, list_keys)

        z = Place()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'Place.destroy("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            instances = storage.all()
            list_keys = []
            for key, obj in instances.items():
                list_keys.append(key)
            self.assertNotIn(id, list_keys)

        z = Amenity()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'Amenity.destroy("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            instances = storage.all()
            list_keys = []
            for key, obj in instances.items():
                list_keys.append(key)
            self.assertNotIn(id, list_keys)

        z = Review()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = 'Review.destroy("{id}")'
            HBNBCommand().onecmd(inppt)  # excute command
            instances = storage.all()
            list_keys = []
            for key, obj in instances.items():
                list_keys.append(key)
            self.assertNotIn(id, list_keys)


class TestUpdate(unittest.TestCase):

    def test_update(self):
    
        z = BaseModel()
        id = z.id
        z.name = "betty"
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update BaseModel {id} name base1'
            HBNBCommand().onecmd(inppt)  # excute command
            self.assertEqual(z.name, "base1")

        z = User()
        id = z.id
        z.first_name = "betty"
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update User {id} first_name John'
            HBNBCommand().onecmd(inppt)  # excute command
            self.assertEqual(z.first_name, "John")

        z = State()
        id = z.id
        z.name = "betty"
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update User {id} name NYC'
            HBNBCommand().onecmd(inppt)  # excute command
            self.assertEqual(z.name, "NYC")

        z = City()
        id = z.id
        z.name = "betty"
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update User {id} name NYC'
            HBNBCommand().onecmd(inppt)  # excute command
            self.assertEqual(z.name, "NYC")

        z = Place()
        id = z.id
        z.name = "betty"
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update Place {id} name NYC'
            HBNBCommand().onecmd(inppt)  # excute command
            self.assertEqual(z.name, "NYC")

        z = Amenity()
        id = z.id
        z.name = "betty"
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update Amenity {id} name NYC'
            HBNBCommand().onecmd(inppt)  # excute command
            self.assertEqual(z.name, "NYC")

        z = Review()
        id = z.id
        z.text = "betty"
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update Place {id} text NYC'
            HBNBCommand().onecmd(inppt)  # excute command
            self.assertEqual(z.text, "NYC")

    def test_update_errors(self):
        """ test errors for update function """
        z = BaseModel()
        id = z.id
        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update BaseModel 123112 name base1'
            HBNBCommand().onecmd(inppt)  # excute command
            expected_output = "** no instance found **"
            self.assertEqual(output.getvalue().strip(), expected_output)

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update BaseModel'
            HBNBCommand().onecmd(inppt)  # excute command
            expected_output = "** instance id missing **"
            self.assertEqual(output.getvalue().strip(), expected_output)

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update base {z.id} name base1'
            HBNBCommand().onecmd(inppt)  # excute command
            expected_output = "** class doesn't exist **"
            self.assertEqual(output.getvalue().strip(), expected_output)

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update'
            HBNBCommand().onecmd(inppt)  # excute command
            expected_output = "** class name missing **"
            self.assertEqual(output.getvalue().strip(), expected_output)

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update BaseModel {z.id}'
            HBNBCommand().onecmd(inppt)  # excute command
            expected_output = "** attribute name missing **"
            self.assertEqual(output.getvalue().strip(), expected_output)

        with patch("sys.stdout", new=StringIO()) as output:
            inppt = f'update BaseModel {z.id} name'
            HBNBCommand().onecmd(inppt)  # excute command
            expected_output = "** value missing **"
            self.assertEqual(output.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()