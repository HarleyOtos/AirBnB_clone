#!/usr/bin/python3
"""Base model module
This module is the module in charge of referencing the rest of
the classes of the AirBnB Clone from which it will be possible
to extract data such as: Unique Universal Identifier (UUID),
date and time instances where a class was created & updated,
standard format to print a class content, to save data created
from instances and the representation of all the keys and
values of an instance. 
"""

from datetime import datetime
import models
import uuid

class BaseModel:
    """
    Base model class is the Base Model that take cares of the
    initialization, serialization & deserialization of future
    instances.

    Attributes:
        id (str): It is the UUID for which an instance is created.
        created_at (datetime): The current datetime when
            an instance is created.
        updated_at (datetime): The current datetime when an instance
            is created and it will be updated every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """
        Base model __init__ method is the default values
        of the Base Model instances are initialized.
        """
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, val)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = self.created_at
                    models.storage.new(self)

    def __str__(self):
        """ Class for user

        Example:
            $ bm = BaseModel()
            $ print(bm)

            The method above print the content of the Base Model
            in the following format

            $ [<class name>] (<self.id>) <self.__dict__>
        """
        return '[{0}] ({1}) {2}'.format(
            self.__class__.__name__, self.id, self.__dict__
        )
    
    def save(self):
        """
        updates the public instance attribute `updated_at` with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Coverts the data to human-readable information

        returns a dictionary containing all keys/values of
        `__dict__` of the instance.
        """
        class_info = self.__dict__.copy()
        class_info['__class__'] = self.__class__.__name__
        class_info['created_at'] = self.created_at.isoformat()
        class_info['updated_at'] = self.updated_at.isoformat()

        return class_info
