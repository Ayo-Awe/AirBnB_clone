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

    def test_create_from_dict(self):
        """
        Test that a new instance is successfully created from
        a dictionary using kwargs
        """

        base = BaseModel()
        base_dict = base.to_dict()

        new_base = BaseModel(**base_dict)

        self.assertEqual(base.created_at, new_base.created_at)
        self.assertEqual(base.id, new_base.id)
        self.assertEqual(base.created_at, new_base.created_at)
        self.assertEqual(str(base), str(new_base))

    def test_ignore_args(self):
        """
        Test that args supplied when creating a
        new instance are ignored
        """

        base = BaseModel()
        base_dict = base.to_dict()

        new_base = BaseModel("hello", **base_dict)

        self.assertEqual(base.created_at, new_base.created_at)
        self.assertEqual(base.id, new_base.id)
        self.assertEqual(base.created_at, new_base.created_at)

    def test_copy_all_dict_keys(self):
        """
        Test that all dictionary keys are
        copied to the new object including extra keys
        """

        base = BaseModel()
        base.name = "tinubu"
        base.friend = "Dami"

        base_dict = base.to_dict()

        new_base = BaseModel(**base_dict)

        self.assertEqual(base.created_at, new_base.created_at)
        self.assertEqual(base.id, new_base.id)
        self.assertEqual(new_base.name, "tinubu")
        self.assertEqual(new_base.friend, "Dami")
        self.assertEqual(base.created_at, new_base.created_at)

    def test_class_not_copied(self):
        """
        Test that the __class__ attribute from
        the dictionary was not copied
        """

        base = BaseModel()
        base_dict = base.to_dict()
        base_dict["__class__"] = "MySomeClass"

        new_base = BaseModel(**base_dict)
        self.assertNotEqual(new_base.__class__, base_dict["__class__"])

    def test_missing_keys(self):
        """
        Test that an error is thrown when accessing attributes that weren't
        set when creating from dictionary
        """

        base = BaseModel()
        base_dict = {"id": "something"}

        new_base = BaseModel(**base_dict)

        with self.assertRaises(Exception):
            val = new_base.created_at
            val = new_base.updated_at


if __name__ == "__main__":
    unittest.main()
