# -*- coding: utf-8 -*-
# para codificar en utf-8
# models.py
from app import app, mongo, db

class Passwords(db.Document):
    """ Class para almacenar usuarios
    """
    email = db.StringField(max_lengt=120)
    user = db.StringField(max_length=120, required=True)
    password = db.StringField(required = True)


    meta = {
        'collection': 'Usuarios',
        'ordering': 'user',
        }

class Post(db.Document):
    ''' Class for defining structure of reddit-top-posts collection
    '''
    url = db.URLField(required=True)
    date = db.DateTimeField(required=True)
    date_str = db.StringField(max_length=10, required=True)
    commentsUrl = db.URLField(required=True)
    sub = db.StringField(max_length=20, required=True) # subredit can be 20 chars
    title = db.StringField(max_length=300, required=True) # title can be 300 chars
    score = db.IntField(required=True)

    meta = {
        'collection': 'top_reddit_posts', # collection name
        'ordering': ['-score'], # default ordering
        'auto_create_index': False, # MongoEngine will not create index
        }
