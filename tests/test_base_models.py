#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBase(unittest.TestCase):
    def test_id_gen(self):
        """Testing the id generation if they are different"""
        mod1 = BaseModel()
        mod2 = BaseModel()
        self.assertNotEqual(mod1.id, mod2.id)

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



if __name__ == "__main__":
    unittest.main()
