#!/usr/bin/env python3
"""
unction that returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find by topic
    Return:
    a  list of school 

    """
    return mongo_collection.find({"topics": topic})
