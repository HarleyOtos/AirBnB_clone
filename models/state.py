#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The State Module is inherits from the BaseModel class.
It contains the attributes that assigned the States.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """The State class
    
    Attributes:
        name (str): The name of a State

    """
    name = ''
