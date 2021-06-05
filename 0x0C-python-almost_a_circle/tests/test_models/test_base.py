#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Test for correct instancing of base object."""
        base_1 = Base(20)

        self.assertIsInstance(base_1, Base)

    def test_id(self):
        """Test for correct instance id assignment"""
        base_1 = Base()
        base_2 = Base(91)
        base_3 = Base()
        base_4 = Base(10)

        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 91)
        self.assertEqual(base_3.id, 2)
        self.assertEqual(base_4.id, 10)
