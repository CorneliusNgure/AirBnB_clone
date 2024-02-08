#!/usr/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        instance = BaseModel()

        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.created_at)
        self.assertIsNotNone(instance.updated_at)

    def test_save(self):
        instance = BaseModel()

        prev_updated_at = instance.updated_at
        current_updated_at = instance.save()

        self.assertNotEqual(prev_updated_at, current_updated_at)

    def test_to_dict(self):
        instance = BaseModel()

        instance_dict = instance.to_dict()

        self.assertIsInstance(instance_dict, dict)

        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertEqual(instance_dict["created_at"], instance.created_at.isoformat())
        self.assertEqual(instance_dict["updated_at"], instance.updated_at.isoformat())

    def test_str(self):
        instance = BaseModel()

        self.assertTrue(str(instance).startswith("[BaseModel]"))
        self.assertIn(instance.id, str(instance))
        self.assertIn(str(instance.__dict__), str(instance))

if __name__ == "__main__":
    unittest.main()
