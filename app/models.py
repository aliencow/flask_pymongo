from app import db
import datetime


class User(db.Document):
    nickname = db.StringField( max_length=64 )
	email = db.StringField( max_length=120, unique=True, required=True )
	created = db.DateTimeField( default=datetime.datetime.utcnow ) # utc to keep it universal
