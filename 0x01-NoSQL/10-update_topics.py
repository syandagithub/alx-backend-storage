#!/usr/bin/env python3
'''Task 10 module.'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a collection's.'''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
