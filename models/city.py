#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The City Module is inherited from the BaseModel class.
It contains the attributes that is assigned to cities.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """The City class
    
    Attributes:
        state_id (str): The UUID of the City it belongs to
        name (str): The city name
    """
    state_id = ''
    name = ''
