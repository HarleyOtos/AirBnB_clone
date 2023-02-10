#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The Review Module is inherited from the BaseModel class.
It contains the attributes that is assigned to Reviews of places
added by users.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The Review Class
    
    Attributes:
        place_id (str): The UUID of the place the review
        belongs to.
        user_id (str): The UUID of the user leaving the review
        text (str): The review the user wrote about the place. 
    """
    place_id = ''
    user_id = ''
    text = ''
