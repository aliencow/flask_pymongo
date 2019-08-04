# -*- coding: utf-8 -*-
# para codificar en utf-8

# basado en videotutorial en https://www.youtube.com/watch?v=rGER0KDdJqI
# combinado con este otro https://www.youtube.com/watch?v=GjJbaolBPAY

from flask import Flask
# importamos Flask
from flask_pymongo import PyMongo
# importamos pymongo
from flask_cors import CORS
# para ejecutar codigo seguro
from flask_bcrypt import Bcrypt
# para encpriptar contraseñas etc
import urllib
# para obviar el error de la @ en el nombre de ususario
from flask_mongoengine import MongoEngine
# para usar los objetos de mongoengine



app = Flask(__name__)
# así se define la entrada de la aplicacion de Flask
CORS(app)
# para evitar intrusos cuestion de  (desactivado por el momento)
bcrypt = Bcrypt(app)
# activamos la variable de encriptación por lo que pueda pasar

app.config['MONGO_DBNAME'] = 'connect_to_mongo'
# configuramos el nombre de la base de datos se accede con la variable mongo.db

app.config['MONGO_URI'] = 'mongodb://'+ urllib.parse.quote("juan.nouche@gmail.com") +':cuatro44@ds143293.mlab.com:43293/connect_to_mongo'
# configuramos la ubicacion de la base en mlab (aparece en pantalla)
# aquí se usa el urllib para el tema de arroba en el nombre de usuario

mongo = PyMongo(app)
# conectamos con la base de datos nuestra app

db = MongoEngine(app)



from app import routes
