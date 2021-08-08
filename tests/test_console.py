#!/usr/bin/python3
""" Console module tests """

import unittest
import cmd
import pep8
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ Testing the console """
    def test_object_creation(self):
        """ Testing the creation of objects """
        self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        self.assertFalse(HBNBCommand().onecmd("create City"))
        self.assertFalse(HBNBCommand().onecmd("create User"))
        self.assertFalse(HBNBCommand().onecmd('create State name="California"'))
        self.assertFalse(HBNBCommand().onecmd("create Review"))
        self.assertFalse(HBNBCommand().onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297'))
    
    def test_pep8(self):
        '''Testing pep8'''
        pep_res = pep8.StyleGuide().check_files(['console.py'])
        self.assertEqual(pep_res.total_errors, 0)
