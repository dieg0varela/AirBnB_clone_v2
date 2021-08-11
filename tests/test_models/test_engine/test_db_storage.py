#!/usr/bin/python3
""" Module for testing db storage"""
from models.amenity import Amenity
import unittest
from models.city import City
from models.base_model import Base, BaseModel
from models import storage
import MySQLdb
import os
import pep8


class test_dbStorage(unittest.TestCase):
    """ Class to test the file storage method """
    __engine = None
    __cursor = None

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def setUp(self):
        """Class constructor"""
        self.__engine = MySQLdb.connect(os.getenv("HBNB_MYSQL_HOST"),
                                              os.getenv("HBNB_MYSQL_USER"),
                                              os.getenv("HBNB_MYSQL_PWD"),
                                              os.getenv("HBNB_MYSQL_DB")
                                        )
        if (os.getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)
        self.__cursor = self.__engine.cursor()

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_new(self):
        """ New object is correctly added to db """
        self.__cursor.execute("SELECT * FROM amenities")
        len_1 = len(self.__cursor.fetchall())
        self.__cursor.execute("INSERT INTO amenities (name) VALUES('Free Nuka-Cola')")
        len_2 = len(self.__cursor.fetchall())
        self.assertNotEqual(len_1, len_2)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_all(self):
        """ db objects are properly returned """
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_save(self):
        """ db save method """
        California_id = self.__cursor.execute("SELECT id FROM states WHERE name='California'")
        New_Vegas_row = City(name="New Vegas", state_id=California_id)
        storage.new(New_Vegas_row)
        storage.save()

        cities_rows = self.__cursor.execute("SELECT name FROM cities").fetchall()

        self.assertTrue("New Vegas" in cities_rows)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE")=="db")
    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
