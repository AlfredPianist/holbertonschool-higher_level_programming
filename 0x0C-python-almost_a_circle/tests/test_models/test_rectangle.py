#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for rectangle.py"""
from unittest import TestCase, mock
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Test for correct instancing and inheritance of rectangle object."""
        rectangle_1 = Rectangle(10, 12)

        self.assertIsInstance(rectangle_1, Rectangle)
        self.assertTrue(issubclass(type(rectangle_1), Base), True)

    def test_attributes(self):
        """Test for correct instance attribute assignment"""
        rectangle_1 = Rectangle(20, 40)

        self.assertEqual(rectangle_1.id, 1)
        self.assertEqual(rectangle_1.width, 20)
        self.assertEqual(rectangle_1.height, 40)
        self.assertEqual(rectangle_1.x, 0)
        self.assertEqual(rectangle_1.y, 0)

        rectangle_2 = Rectangle(1, 20, 2, 4, 20)

        self.assertEqual(rectangle_2.id, 20)
        self.assertEqual(rectangle_2.width, 1)
        self.assertEqual(rectangle_2.height, 20)
        self.assertEqual(rectangle_2.x, 2)
        self.assertEqual(rectangle_2.y, 4)

        rectangle_3 = Rectangle(4, 1, 33, 4)

        self.assertEqual(rectangle_3.id, 2)
        self.assertEqual(rectangle_3.width, 4)
        self.assertEqual(rectangle_3.height, 1)
        self.assertEqual(rectangle_3.x, 33)
        self.assertEqual(rectangle_3.y, 4)

    def test_raise_argument_errors(self):
        """Test for correct argument error output"""
        with self.assertRaises(TypeError) as exc:
            Rectangle(1)
        self.assertEqual(str(exc.exception),
                         "__init__() missing 1 required positional argument:" +
                         " 'height'")

        with self.assertRaises(TypeError) as exc:
            Rectangle()
        self.assertEqual(str(exc.exception),
                         "__init__() missing 2 required positional " +
                         "arguments: 'width' and 'height'")

    def test_raise_type_errors(self):
        """Test for correct type error output"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"world": 4})

    def test_raise_value_errors(self):
        """Test for correct value error output"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(4, 2, -1, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(8, 10, 5, -4)

    def test_area(self):
        """Test for correct area calculation"""
        rectangle_1 = Rectangle(10, 40)

        self.assertEqual(rectangle_1.area(), 400)

    def test_print_no_offset(self):
        """Test for correct rectangle printing without offset"""
        rectangle_1 = Rectangle(5, 4)
        correct_output = "#####\n#####\n#####\n#####\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            rectangle_1.display()
            self.assertEqual(output.getvalue(), correct_output)

        rectangle_2 = Rectangle(2, 6)
        correct_output = "##\n##\n##\n##\n##\n##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            rectangle_2.display()
            self.assertEqual(output.getvalue(), correct_output)

    def test_print_with_offset(self):
        """Test for correct rectangle printing with offset"""
        rectangle_1 = Rectangle(5, 4, 3, 2)
        correct_output = "\n\n   #####\n   #####\n   #####\n   #####\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            rectangle_1.display()
            self.assertEqual(output.getvalue(), correct_output)

        rectangle_2 = Rectangle(2, 6, 0, 4)
        correct_output = "\n\n\n\n##\n##\n##\n##\n##\n##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            rectangle_2.display()
            self.assertEqual(output.getvalue(), correct_output)

        rectangle_2.x = 2
        rectangle_2.y = 0
        correct_output = "  ##\n  ##\n  ##\n  ##\n  ##\n  ##\n"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            rectangle_2.display()
            self.assertEqual(output.getvalue(), correct_output)

    def test_str_magic_method(self):
        """Test for correct __str__ output"""
        rectangle_1 = Rectangle(1, 2)
        correct_output = "[Rectangle] (1) 0/0 - 1/2"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_2 = Rectangle(4, 6, 2, 3, 21)
        correct_output = "[Rectangle] (21) 2/3 - 4/6"
        self.assertEqual(rectangle_2.__str__(), correct_output)

    def test_update_args(self):
        """Test for correct update method with args"""
        rectangle_1 = Rectangle(2, 2, 2, 2, 2)
        correct_output = "[Rectangle] (2) 2/2 - 2/2"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update(10)
        correct_output = "[Rectangle] (10) 2/2 - 2/2"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update(10, 4)
        correct_output = "[Rectangle] (10) 2/2 - 4/2"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update(10, 4, 6)
        correct_output = "[Rectangle] (10) 2/2 - 4/6"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update(10, 4, 6, 8)
        correct_output = "[Rectangle] (10) 8/2 - 4/6"
        self.assertEqual(rectangle_1.__str__(), correct_output)

        rectangle_1.update(10, 4, 6, 8, 12)
        correct_output = "[Rectangle] (10) 8/12 - 4/6"
        self.assertEqual(rectangle_1.__str__(), correct_output)

    def test_update_kwargs(self):
        """Test for correct update method with kwargs"""
        rectangle_2 = Rectangle(2, 2, 2, 2, 2)
        correct_output = "[Rectangle] (2) 2/2 - 2/2"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(id=10)
        correct_output = "[Rectangle] (10) 2/2 - 2/2"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(width=4, id=10)
        correct_output = "[Rectangle] (10) 2/2 - 4/2"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(id=10, height=6, width=4)
        correct_output = "[Rectangle] (10) 2/2 - 4/6"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(x=8, width=4, height=6)
        correct_output = "[Rectangle] (10) 8/2 - 4/6"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(y=12, id=10, x=8, height=6, width=4)
        correct_output = "[Rectangle] (10) 8/12 - 4/6"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2.update(12, 200, y=8, x=15)
        correct_output = "[Rectangle] (12) 8/12 - 200/6"
        self.assertEqual(rectangle_2.__str__(), correct_output)

        rectangle_2_pre_update = rectangle_2.__dict__
        rectangle_2.update(fake=30)
        self.assertEqual(rectangle_2.__dict__, rectangle_2_pre_update)

    def test_to_dictionary(self):
        """Test for correct to_dictionary output"""
        rectangle_1 = Rectangle(2, 20)
        rectangle_1_dict = {'id': 1, 'width': 2, 'height': 20, 'x': 0, 'y': 0}
        self.assertEqual(rectangle_1.to_dictionary(), rectangle_1_dict)
        self.assertIsInstance(rectangle_1_dict, dict)

        rectangle_2 = Rectangle(30, 1, 50, 2)
        rectangle_2_dict = {'id': 2, 'width': 30, 'height': 1, 'x': 50, 'y': 2}
        self.assertEqual(rectangle_2.to_dictionary(), rectangle_2_dict)
        self.assertIsInstance(rectangle_2_dict, dict)

        rectangle_3 = Rectangle(1, 2, 24, 9, 20)
        rectangle_3_dict = {'id': 20, 'width': 1, 'height': 2, 'x': 24, 'y': 9}
        self.assertEqual(rectangle_3.to_dictionary(), rectangle_3_dict)
        self.assertIsInstance(rectangle_3_dict, dict)

        rectangle_3.update(**rectangle_2.to_dictionary())
        self.assertEqual(rectangle_2.__dict__, rectangle_3.__dict__)
