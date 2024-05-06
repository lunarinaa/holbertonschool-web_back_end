#!/usr/bin/env python3
"""Task 10"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    name_ = {name: name}
    set = {"$set": {"topics": topics}}
    mongo_collection.update_many(name, set)
