#!/usr/bin/env python3
"""
a function that list all document
"""
import pymongo


def list_all(mongo_collection):
    """
    list all documents in a collection

    Return:
        an empty list if no document in the collection
    """

    if not mongo_collection:
        return []
    return list(mongo_collection.find())
