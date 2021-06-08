#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""base module.

This is the Base class from which the other classes will be based. It only has
one class attribute __nb_objects serving as a counter of instances, and as
methods, the class constructor, a serialization and deserialization methods
both to and from json and csv, an object creation method from its dictionary
representation and a drawing method using the turtle library.
"""
import json
import csv
import turtle


class Base():
    """A Base class working as superclass of Rectangle."""
    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor.
        Args:
            id (int): The id of the instance. If id is provided, the
                      instance's id will be the one provided. Otherwise, the
                      private class astribute's __nb_objects one will be
                      assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that creates a json string from a list of rectangle
        or square object dictionaries.
        Args:
            list_rectangles (list): A list of rectangle or square dictionaries.
        Returns:
            str: The json string serialization of the rectangle or square
                 dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        # raise exception on non list and dictionary
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Static method that creates a list of object dictionaries from a
        json string.
        Args:
            json_string (str): A string with the json representations of the
                               dictionaries of the objects to be converted.
        Returns:
            list: The list of object dictionaries converted.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance from its dictionary representation.
        Args:
            **dictionary: The dictionary representation of an object's
                          attributes.
        Returns:
            obj: The instance with its attributes passed as keyword arguments.
        """
        instance = cls(1, 1) if cls.__name__ == 'Rectangle' else cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that saves a json file, serializing a list of rectangle
        or square instances.
        Args:
            list_objs (list): A list of objects.
        """
        with open(cls.__name__ + ".json", "w", encoding='utf-8') as f:
            json_strs = []
            if list_objs is not None:
                json_strs = [obj.to_dictionary() for obj in list_objs]
                json_strs = cls.to_json_string(json_strs)
            f.write(str(json_strs))

    @classmethod
    def load_from_file(cls):
        """Class method that loads a json file and returns a list of square
        or rectangle instances (deserialization).
        Returns:
            list: A list of instances of class cls.
        """
        try:
            with open(cls.__name__ + ".json", "r", encoding='utf-8') as f:
                instances_dict = cls.from_json_string(f.read())

            instance_ls = []
            for instance in instances_dict:
                instance_ls.append(cls.create(**instance))
            return instance_ls
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method that saves a csv file, serializing a list of rectangle
        or square instances.
        Args:
            list_objs (list): A list of objects.
        """
        rec_fields = ["id", "width", "height", "x", "y"]
        squ_fields = ["id", "size", "x", "y"]

        with open(cls.__name__ + ".csv", "w",
                  newline='', encoding='utf-8') as f:
            if list_objs is not None:
                if cls.__name__ == "Rectangle":
                    write_csv = csv.DictWriter(f, fieldnames=rec_fields)
                else:
                    write_csv = csv.DictWriter(f, fieldnames=squ_fields)
                csv_rows = [obj.to_dictionary() for obj in list_objs]
                write_csv.writeheader()
                write_csv.writerows(csv_rows)

    @classmethod
    def load_from_file_csv(cls):
        """Class method that loads a csv file and returns a list of square
        or rectangle instances (deserialization).
        Returns:
            list: A list of instances of class cls.
        """
        try:
            with open(cls.__name__ + ".csv", "r",
                      newline='', encoding='utf-8') as f:
                read_csv = csv.DictReader(f)
                instances_dict = []
                for row in read_csv:
                    row = dict([k, int(val)] for k, val in row.items())
                    instances_dict.append(row)

            instance_ls = []
            for instance in instances_dict:
                instance_ls.append(cls.create(**instance))
            return instance_ls
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Static method that draws a list of rectangles and squares using the
        turtle library.
        Args:
            list_rectangles (list): A list of rectangle objects.
            list_squares (list): A list of square objects.
        """
        draw_offset = 20
        t = turtle.Turtle(visible=False)

        print("Drawing rectangles...")

        start = (draw_offset - t.screen.window_width() / 2, 0)
        t.pu()
        t.goto(start[0], start[1])
        t.st()

        stroke_rec = "#0033CC"
        fill_rec = "#007BB4"

        t.pen(pencolor=stroke_rec, fillcolor=fill_rec,
              pensize=5, speed=3)
        max_height = 0
        for idx, rec in enumerate(list_rectangles):
            if ((t.xcor() + rec.x + rec.width) <=
                    (t.screen.window_width() - draw_offset)):
                t.goto(t.xcor() + rec.x + draw_offset, t.ycor())
            else:
                t.clear()
                t.goto(start[0], start[1])
            t.goto(t.xcor() + rec.x, t.ycor() + rec.y)
            t.pd()
            t.begin_fill()
            for i in range(2):
                t.fd(rec.width)
                t.rt(90)
                t.fd(rec.height)
                t.rt(90)
            t.end_fill()
            t.pu()
            t.goto(t.xcor() + rec.width, t.ycor())
            max_height = rec.height if rec.height >= max_height else max_height

        t.pu()
        t.speed(1)
        t.ht()
        t.goto(start[0], start[1])
        t.st()

        stroke_squ = "#D3212D"
        fill_squ = "#D34E2D"

        print("Drawing squares...")
        t.clear()

        t.pen(pencolor=stroke_squ, fillcolor=fill_squ,
              pensize=5, speed=3)
        max_height = 0
        for idx, squ in enumerate(list_squares):
            if ((t.xcor() + squ.x + squ.size) <=
                    (t.screen.window_width() - draw_offset)):
                t.goto(t.xcor() + squ.x + draw_offset, t.ycor())
            else:
                t.clear()
                t.goto(start[0], start[1])
            t.goto(t.xcor() + squ.x, t.ycor() + squ.y)
            t.pd()
            t.begin_fill()
            for i in range(4):
                t.fd(squ.size)
                t.rt(90)
            t.end_fill()
            t.pu()
            t.goto(t.xcor() + squ.size, t.ycor())
            max_height = squ.size if squ.size >= max_height else max_height

        turtle.done()
