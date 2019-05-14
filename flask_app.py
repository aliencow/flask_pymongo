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

import urllib
# para obviar el error de la @ en el nombre de ususario

app = Flask(__name__)
# así se define la entrada de la aplicacion de Flask
CORS(app)
# para evitar intrusos cuestion de seguridad

app.config['MONGO_DBNAME'] = 'connect_to_mongo'
# configuramos el nombre de la base de datos se accede con la variable mongo.db

app.config['MONGO_URI'] = 'mongodb://'+ urllib.quote("juan.nouche@gmail.com") +':cuatro44@ds143293.mlab.com:43293/connect_to_mongo'
# configuramos la ubicacion de la base en mlab (aparece en pantalla)
# aquí se usa el urllib para el tema de arroba en el nombre de usuario

mongo = PyMongo(app)
# conectamos con la base de datos nuestra app

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/wibble')
def wibble():
    return 'This is my pointless new page'

@app.route("/add")
# ruta en la web desde el directorio base
def add(): # definición de la función que se va a ejecutar desde esa ruta (no tiene porque coincidir el nombre)
    #user = mongo.db.users #crea una collection (tabla) users dentro de nuestra base de datos (si no existe ya)
    #user.insert({'name' : 'Manolete', 'Apellido':'AnyWhere'}) # insertamos un document (registro)
    return 'Se ha añadido a Antonio'

