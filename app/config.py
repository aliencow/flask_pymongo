import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'DU3Vwfkn1u9VHXj39T5doC6WnHiifEVv'