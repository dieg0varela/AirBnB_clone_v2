#!/usr/bin/python3
""" Test of the City class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import session, sessionmaker
import pep8


class test_City(test_basemodel):
    """ City class test """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8(self):
        """ Pep8 Style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error")
