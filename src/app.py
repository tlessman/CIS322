from flask import Flask, render_template, request, session, redirect, url_for
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
conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
cur = conn.cursor()

# PATHS #
@app.route('/', methods=['GET'])
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    if request.method =='POST' and ('username' in request.form and 'password' in request.form):
        if not check_username(request.form['username']):
            render_template('create_user.html')
        if verify_password(request.form['username'], request.form['password']):
            session['username']=request.form['username']
            return redirect(url_for('dashboard'))
        else:
            return render_template('invalid_credentials.html')
    return render_template('login.html', dbname=dbname, dbhost=dbhost, dbport=dbport)
#

@app.route('/create_user', methods=['GET','POST'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')
    if request.method == 'POST' and ('username' in request.form and 'password' in request.form): 
        if check_username(request.form['username']):
            return render_template('username_taken.html')
        else:
            SQL = "INSERT INTO users (user_pk, username, password) VALUES (DEFAULT, %s, %s);"
            data = (request.form['username'], request.form['password'],)
            cur.execute(SQL, data)
            conn.commit()
            session['username']=request.form['username']
            return redirect(url_for('dashboard')) 
        #
    #
    return render_template('create_user.html')
#

@app.route('/username_taken')
def user_taken():
    if request.method == 'GET':
        return render_template('user_taken.html')
    if request.method == 'POST' and ('username' in request.form and 'password' in request.form):
        if check_username(request.form['username']): 
            return render_template('username_taken.html')
        else:
            SQL = "INSERT INTO users (user_pk, username, password) VALUES (DEFAULT, %s, %s);"
            data = (request.form['username'], request.form['password'],)
            cur.execute(SQL, data)
            conn.commit()
            session['username']=request.form['username']
            return redirect(url_for("dashboard")) 
        #
    #
    return render_template('user_taken.html')
#

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

        
# HELPERS #        
def check_username(name):
    SQL = "SELECT * FROM users WHERE username=%s;"
    data = (name,)
    cur.execute(SQL, data)
    user_res = cur.fetchall()
    return bool(user_res)
#

def verify_password(name, string):
    SQL = "SELECT * FROM users WHERE username=%s;"
    data = (name,)
    cur.execute(SQL, data)
    user_res = cur.fetchall()
    print(user_res['password'] == string)
    return (user_res['password'] == string)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)
#
