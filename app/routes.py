# -*- coding: utf-8 -*-
# para codificar en utf-8
from flask import render_template
from app import app, mongo
from app.forms import LoginForm



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('form.html', title='Sign In', form=form)

@app.route('/wibble')
def wibble():
    return 'This is my pointless new page'

@app.route("/add")
# ruta en la web desde el directorio base
def add(): # definición de la función que se va a ejecutar desde esa ruta (no tiene porque coincidir el nombre)
    user = mongo.db.users #crea una collection (tabla) users dentro de nuestra base de datos (si no existe ya)
    user.insert({'name' : 'Manolete', 'Apellido':'AnyWhere'}) # insertamos un document (registro)
    return 'Se ha añadido a Manolete'
