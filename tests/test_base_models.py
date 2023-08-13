#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestBase(unittest.TestCase):
    """testing the base_model
        args: unittest
    """
    def setUp(self):
        """testing the process of saving file"""
        with open("test.json", "w"):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """deleteting a created file"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_id_gen(self):
        """Testing the id generation if they are different"""
        mod1 = BaseModel()
        mod2 = BaseModel()
        self.assertNotEqual(mod1.id, mod2.id)
        self.assertIsInstance(mod1.id, str)

    def test_created_at(self):
        """testing created at"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
    
    def test_updated_at(self):
        """testing Update"""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_upates(self):
        """testing save"""
        model = BaseModel()
        upd_at = model.updated_at
        model.save()
        self.assertNotEqual(upd_at, model.updated_at)

    def test_dict_dic(self):
        """testing dict"""
        model = BaseModel()
        ob_dict = model.to_dict()
        self.assertIsInstance(ob_dict, dict)
        self.assertIn('__class__', ob_dict)
        self.assertEqual(ob_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', ob_dict)
        self.assertIn('updated_at', ob_dict)
    def test_base_from_dict(self):
        """Testing task 4, with kwargs init"""
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model_json, my_new_model.to_dict())
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_base_from_emp_dict(self):
        """test with an empty dictionary"""
        my_dict = {}
        my_new_model = BaseModel(**my_dict)
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_base_from_non_dict(self):
        """test with a None dictionary"""
        my_new_model = BaseModel(None)
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_save(self):
        """ test save method of basemodel """
        my_new_model = BaseModel()
        previous = my_new_model.updated_at
        my_new_model.save()
        actual = my_new_model.updated_at
        self.assertTrue(actual > previous)

    def test_isinstance(self):
        """ Check if object is basemodel instance """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_executable_file(self):
        """ Check if file have permissions to execute"""
        is_read_true = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(is_exec_true)


if __name__ == "__main__":
    unittest.main()
