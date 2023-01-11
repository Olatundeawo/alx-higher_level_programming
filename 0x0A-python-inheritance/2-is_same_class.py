#!/usr/bin/python3
"""
Function that check for instance
"""

def is_same_class(obj, a_class):
    """check for maybe instance is equal """
    if isinstance(obj, a_class):
        return True
    else:
        return False
