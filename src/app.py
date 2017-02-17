from flask import Flask, render_template, request, session
#from config import dbname, dbhost, dbport
import psycopg2
#import json
#from datetime import datetime

# GLOBALS #
app = Flask(__name__)
app.secret_key='c34f5286bed45063'
dbname = 'lost'
dbhost = '127.0.0.1'
dbport = 5432
conn = psycopg2.connect(dbname, dbhost, dbport)
cur = conn.cursor()

# PATHS #
@app.route('/')
@app.route('/index)
def index():
    return render_template('index.html', dbname=dbname, dbhost=dbhost, dbport=dbport)

@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html', dbname=dbname, dbhost=dbhost, dbport=dbport)

@app.route('/create_user', methods=['GET','POST'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')
"""
    if request.method == 'POST' and (username in request.form and password in request.form):
        checkusername()

# HELPERS #        
def check_username()

    SQL = "SELECT 1 FROM users WHERE username=%s;"
    data = (request.form['username'],)
    user_exists = cur.execute(SQL, data)
        if user_exists == 1
            return render_template('create_user.html', methods='GET')
        else 
            SQL = "INSERT INTO users (user_pk, username, password) VALUES (DEFAULT, %s, %s);"
            data = (request.form['username'], request.form['password'],)
            cur.execute(SQL, data)
            return
"""
