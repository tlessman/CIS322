from flask import Flask, render_template, request, session
#from config import dbname, dbhost, dbport
import psycopg2
#import json
#from datetime import datetime

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)

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
@app.route('/index')
def index():
    return render_template('index.html', dbname=dbname, dbhost=dbhost, dbport=dbport)

@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html', dbname=dbname, dbhost=dbhost, dbport=dbport)

@app.route('/create_user', methods=['GET','POST'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')

    if request.method == 'POST' and (username in request.form and password in request.form):
    
    if check_username() 
        return render_template('create_user.html', methods='GET')
    else 
        SQL = "INSERT INTO users (user_pk, username, password) VALUES (DEFAULT, %s, %s);"
        data = (request.form['username'], request.form['password'],)
        cur.execute(SQL, data)
        cur.commit()
        
# HELPERS #        
def check_username()

    SQL = "SELECT 1 FROM users WHERE username=%s;"
    data = (request.form['username'],)
    cur.execute(SQL, data)
    user_res = cur.fetchall()
    return bool(user_res)


