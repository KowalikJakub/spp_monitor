import requests
import os
import json
from flask import Flask, render_template, \
                        url_for, jsonify, request, redirect, abort
from flask_login import LoginManager

from routing import PrefixedRouteBuilder

app = Flask(__name__)
login_manager = LoginManager(app=app)

router = PrefixedRouteBuilder('')

@app.route(router.create('index'))
def index():
    return render_template('index.html')

@app.route(router.create('login'), methods=['GET'])
def login_page():
    return render_template('login.html',
                           submit_route=router.create('auth'))

@app.route(router.create('auth'), methods=['POST'])
def login():
    password = request.form['pwd']
    username = request.form['usr']

    if not ((username == "root") and (password == "toor")):
        return redirect(router.create('login'), 404)
    return redirect(router.create('index'))
