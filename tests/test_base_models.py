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
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
    
    def test_updated_at(self):
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_upates(self):
        model = BaseModel()
        upd_at = model.updated_at
        model.save()
        self.assertNotEqual(upd_at, model.updated_at)

    def test_dict_dic(self):
        model = BaseModel()
        ob_dict = model.to_dict()
        self.assertIsInstance(ob_dict, dict)
        self.assertIn('__class__', ob_dict)
        self.assertEqual(ob_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', ob_dict)
        self.assertIn('updated_at', ob_dict)


if __name__ == "__main__":
    unittest.main()
