#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module to find the max integer in a list
"""
import unittest
import os
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 50, 2, 10]), 50)
        self.assertEqual(max_integer([-1, -20, -2, -50]), -1)
        self.assertEqual(max_integer("1 2 3 4 5"), '5')
        self.assertEqual(max_integer((40, 0, 2, 5)), 40)
        self.assertEqual(max_integer((10, 0,- 2, 5)), 10)
        self.assertEqual(max_integer([40]), 40)
        self.assertEqual(max_integer([]), None)

    def test_types(self):
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 1234)

    def test_doc(self):
        self.assertTrue(len(max_integer.__doc__) > 8)
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 8)
