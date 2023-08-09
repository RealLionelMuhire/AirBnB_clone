#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseInit(unittest.TestCase):
    def test_id_gen(self):
        """Testing the id generation if they are different"""
        mod1 = BaseModel()
        mod2 = BaseModel()
        self.assertNotEqual(mod1.id, mod2.id)

    def test_created_at(self):
        model = BaseModel()
        self.assertTrue(model.created_at == datetime.now())
    
    def test_updated_at(self):
        model = BaseModel()
        self.assertTrue(model.updated_at == datetime.now())


if __name__ == "__main__":
    unittest.main()
