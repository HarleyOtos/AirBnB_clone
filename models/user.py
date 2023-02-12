#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The User Module is the module that inherits from the
BaseModel class. It contain user(s) information.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """The User class

    Attributes:
        email (str): The email of User
        password (str): The password of a User
        first_name (str): The first name of a User
        last_name (str): The last name of a User
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
