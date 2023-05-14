#!/usr/bin/python3
"""defines a file storage class"""
import json

class FileStorage:
    """file storage class"""
    __file__path  = "file.json"
    __objects = {}

def all(self):
    """returns the dictionary __objects"""
     return FileStorage.__objects

def new(self, obj):
    """sets the obj with key"""
    obj_class_name = obj.__class__.__name__
    obj_id = obj.id
    key_name = obj_class_name + "." + obj_id
    obj = FileStorage.__objects[key_name]
    return obj
