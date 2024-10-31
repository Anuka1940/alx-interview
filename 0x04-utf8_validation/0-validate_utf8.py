#!/usr/bin/python3
"""
 method that determines if a given data set
 represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    if isinstance(data, list):
        if not all(0 <= byte <= 255 for byte in data):
            return False
        else:
            return True
