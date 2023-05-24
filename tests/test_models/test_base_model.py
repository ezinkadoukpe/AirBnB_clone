#!/usr/bin/python3

"""Test for BaseModel"""

import unittest
from models.base_model import BaseModel
import pep8
import os


class TestBaseModel(unittest.TestCase):
    """A class to test the base model class"""
    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.baseMod = BaseModel()
        cls.baseMod.name = "Vital"
        cls.baseMod.num = 56

    @classmethod
    def teardown(cls):
        """ tear it down"""
        del cls.baseMod

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        styl = pep8.StyleGuide(quiet=True)
        c = styl.check_files(['models/base_model.py'])
        self.assertEqual(c.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """checking if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))


if __name__ == "__main__":
    unittest.main()
