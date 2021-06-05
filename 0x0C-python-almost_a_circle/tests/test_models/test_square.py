#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for square.py"""
from unittest import TestCase, mock
from io import StringIO
from models.base import Base
from models.square import Square


class TestSquare(TestCase):
    """Test cases for Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Test for correct instancing and inheritance of square object."""
        square_1 = Square(10, 12)

        self.assertIsInstance(square_1, Square)
        self.assertTrue(issubclass(type(square_1), Base), True)

    def test_attributes(self):
        """Test for correct instance attribute assignment"""
        square_1 = Square(20)

        self.assertEqual(square_1.id, 1)
        self.assertEqual(square_1.width, 20)
        self.assertEqual(square_1.height, 20)
        self.assertEqual(square_1.x, 0)
        self.assertEqual(square_1.y, 0)

        square_2 = Square(1, 2, 4, 20)

        self.assertEqual(square_2.id, 20)
        self.assertEqual(square_2.width, 1)
        self.assertEqual(square_2.height, 1)
        self.assertEqual(square_2.x, 2)
        self.assertEqual(square_2.y, 4)

        square_3 = Square(4, 1, 33)

        self.assertEqual(square_3.id, 2)
        self.assertEqual(square_3.width, 4)
        self.assertEqual(square_3.height, 4)
        self.assertEqual(square_3.x, 1)
        self.assertEqual(square_3.y, 33)

    def test_raise_argument_errors(self):
        """Test for correct argument error output"""
        with self.assertRaises(TypeError) as exc:
            Square()
        self.assertEqual(str(exc.exception),
                         "__init__() missing 1 required positional " +
                         "argument: 'size'")

    def test_raise_type_errors(self):
        """Test for correct type error output"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None, 3, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {"world": 4})

    def test_raise_value_errors(self):
        """Test for correct value error output"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(4, -1, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(8, 5, -4)

    def test_area(self):
        """Test for correct area calculation"""
        square_1 = Square(10)

        self.assertEqual(square_1.area(), 100)

    def test_print_no_offset(self):
        """Test for correct square printing without offset"""
        square_1 = Square(5)
        correct_output = "#####\n#####\n#####\n#####\n#####\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            square_1.display()
            self.assertEqual(output.getvalue(), correct_output)

        square_2 = Square(2)
        correct_output = "##\n##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            square_2.display()
            self.assertEqual(output.getvalue(), correct_output)

    def test_print_with_offset(self):
        """Test for correct square printing with offset"""
        square_1 = Square(4, 3, 2)
        correct_output = "\n\n   ####\n   ####\n   ####\n   ####\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            square_1.display()
            self.assertEqual(output.getvalue(), correct_output)

        square_2 = Square(2, 0, 4)
        correct_output = "\n\n\n\n##\n##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            square_2.display()
            self.assertEqual(output.getvalue(), correct_output)

        square_2.x = 2
        square_2.y = 0
        correct_output = "  ##\n  ##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            square_2.display()
            self.assertEqual(output.getvalue(), correct_output)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        square_1 = Square(2)
        correct_output = "[Square] (1) 0/0 - 2"
        self.assertEqual(square_1.__str__(), correct_output)

        square_2 = Square(4, 6, 3, 21)
        correct_output = "[Square] (21) 6/3 - 4"
        self.assertEqual(square_2.__str__(), correct_output)

    def test_update_args(self):
        """Test for correct update method with args"""
        square_1 = Square(2, 2, 2, 2)
        correct_output = "[Square] (2) 2/2 - 2"
        self.assertEqual(square_1.__str__(), correct_output)

        square_1.update(10)
        correct_output = "[Square] (10) 2/2 - 2"
        self.assertEqual(square_1.__str__(), correct_output)

        square_1.update(10, 4)
        correct_output = "[Square] (10) 2/2 - 4"
        self.assertEqual(square_1.__str__(), correct_output)

        square_1.update(10, 4, 6)
        correct_output = "[Square] (10) 6/2 - 4"
        self.assertEqual(square_1.__str__(), correct_output)

        square_1.update(10, 4, 6, 8)
        correct_output = "[Square] (10) 6/8 - 4"
        self.assertEqual(square_1.__str__(), correct_output)

    def test_update_kwargs(self):
        """Test for correct update method with kwargs"""
        square_2 = Square(2, 2, 2, 2)
        correct_output = "[Square] (2) 2/2 - 2"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2.update(id=10)
        correct_output = "[Square] (10) 2/2 - 2"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2.update(width=4, id=10)
        correct_output = "[Square] (10) 2/2 - 4"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2.update(id=10, x=6, width=4)
        correct_output = "[Square] (10) 6/2 - 4"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2.update(y=8, width=4, x=6)
        correct_output = "[Square] (10) 6/8 - 4"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2.update(1, 2, y=100)
        correct_output = "[Square] (1) 6/8 - 2"
        self.assertEqual(square_2.__str__(), correct_output)

        square_2_pre_update = square_2.__dict__
        square_2.update(fake=30)
        self.assertEqual(square_2.__dict__, square_2_pre_update)

    def test_to_dictionary(self):
        """Test for correct to_dictionary output"""
        square_1 = Square(2)
        square_1_dict = {'id': 1, 'size': 2, 'x': 0, 'y': 0}
        self.assertEqual(square_1.to_dictionary(), square_1_dict)
        self.assertIsInstance(square_1_dict, dict)

        square_2 = Square(30, 50, 2)
        square_2_dict = {'id': 2, 'size': 30, 'x': 50, 'y': 2}
        self.assertEqual(square_2.to_dictionary(), square_2_dict)
        self.assertIsInstance(square_2_dict, dict)

        square_3 = Square(1, 24, 9, 20)
        square_3_dict = {'id': 20, 'size': 1, 'x': 24, 'y': 9}
        self.assertEqual(square_3.to_dictionary(), square_3_dict)
        self.assertIsInstance(square_3_dict, dict)

        square_3.update(**square_2.to_dictionary())
        self.assertEqual(square_2.__dict__, square_3.__dict__)
