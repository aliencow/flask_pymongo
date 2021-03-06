# -*- coding: utf-8 -*-
# para codificar en utf-8
from flask import render_template, flash, redirect
from app import app, mongo
from app.forms import LoginForm
import lorem

"""
s = lorem.sentence()  # 'Eius dolorem dolorem labore neque.'
p = lorem.paragraph()
t = lorem.text()
"""

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nouchocks'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Una superprueba de uso de datos en web!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    ipsum = lorem.text()
    return render_template('index.html', title='Home', user=user, posts=posts, ipsum = ipsum)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('form.html', title='Sign In', form=form)


@app.route('/wibble')
def wibble():
    flash('Acabas de entrar en wibble')
    return 'This is my pointless new page'

@app.route("/add")
# ruta en la web desde el directorio base
def add(): # definición de la función que se va a ejecutar desde esa ruta (no tiene porque coincidir el nombre)
    user = mongo.db.users #crea una collection (tabla) users dentro de nuestra base de datos (si no existe ya)
    user.insert({'name' : 'Manolete', 'Apellido':'AnyWhere'}) # insertamos un document (registro)
    return 'Se ha añadido a Manolete'
