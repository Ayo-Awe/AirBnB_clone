#!/usr/bin/python3
"""Test module for base model"""

from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBase(unittest.TestCase):
    """Test module for base class"""

    def test_attributes(self):
        """
        Test that public attributes are set and are of
        the right type
        """
        base = BaseModel()

        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertIsInstance(base.id, str)

        self.assertEqual(len(base.id), 36)

    def test_save(self):
        """
        Test that save function updates updated_at
        """
        base = BaseModel()

        last_updated = base.updated_at
        base.save()

        self.assertIsInstance(base.updated_at, datetime)
        self.assertNotEqual(base.updated_at, last_updated)

    def test_to_dict(self):
        """
        Test that to_dict function generates the expected python
        dictionary
        """
        base = BaseModel()
        base_dict = base.to_dict()

        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["created_at"], base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"], base.updated_at.isoformat())
        self.assertEqual(base_dict["id"], base.id)
        self.assertEqual(base_dict["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
