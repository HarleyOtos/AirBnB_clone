#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The Amenity Module is inherited from the BaseModel class.
It contains the attributes that is assigned to Amenities
of places.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity class
    
    Attributes:
        name (str): The name of the Amenity
    """
    name = ''
