from flask import Flask, render_template, request, session, redirect, url_for
from config import dbname, dbhost, dbport
import psycopg2
import json
#from datetime import datetime

# GLOBALS #
app = Flask(__name__)
app.secret_key='c34f5286bed45063'
#dbname = 'lost' 
#dbhost = '127.0.0.1'
#dbport = 5432
conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
cur = conn.cursor()
#session['logged_in'] = FALSE


# PATHS #
@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='GET':
        #session['error'] = ""
        return render_template('login.html')
    if request.method =='POST' and ('username' in request.form and 'password' in request.form):
        if not check_username(request.form['username']):
            #session['error'] = "Username does not exist."
            return redirect(url_for('login'))
        if verify_password(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            cur.execute("SELECT role FROM users WHERE username = %s;"%(username))
            res = cur.fetchone()
            session['role'] = res
            session['logged_in'] = TRUE
            return redirect(url_for('dashboard'))
        else:
            session['error'] = "Invalid password."
            return redirect(url_for('invalid_credentials'))
    return render_template('login.html', dbname=dbname, dbhost=dbhost, dbport=dbport)
#

@app.route('/create_user', methods=['GET','POST'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')
    if request.method == 'POST' and ('username' in request.form and 'password' in request.form): 
        if check_username(request.form['username']):
            session['error'] = "Username already exists."
            return redirect(url_for('username_taken'))
        else:
            username = request.form['username']
            password = request.form['password']
            role = request.form['role']
            cur.execute("INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, '%s', '%s', '%s', TRUE);"%(username,password,role))
            conn.commit() 
            return redirect(url_for('login')) 
        #
    #
    return render_template('create_user.html')
#

@app.route('/username_taken', methods = ['GET', 'POST'])
def username_taken():
    if request.method == 'POST' and ('username' in request.form and 'password' in request.form):
        if check_username(request.form['username']): 
            return redirect(url_for('create_user'))
#        else:
#            SQL = "INSERT INTO users (user_pk, username, password, role, active,) VALUES (DEFAULT, %s, %s, %s, TRUE,);"
#            data = (request.form['username'], request.form['password'], request.form['role'],)
#            cur.execute(SQL, data)
#            conn.commit()
#            session['username']=request.form['username']
#            SQL = "SELECT role FROM users WHERE usename = %s;"
#            data = session['username']
#            cur.execute(SQL, data)
#            role_res = cur.fetchone()
#            session['role']=role_res
#            return redirect(url_for('dashboard')) 

        #
    #
    return render_template('create_user.html')
#

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    #if session['logged_in'] == FALSE:
    #    session['error'] = "Unauthorized access."
    #    return redirect(url_for("login"))
    return render_template('dashboard.html')

@app.route('/add_facility', methods=['GET','POST'])
def add_facility():
    if request.method == 'GET':
        return render_template('add_facility.html')
    if request.method == 'POST' and ('fcode' in request.form and 'common_name' in request.form):
        #SQL
        fcode = request.form['fcode']
        common_name = request.form['common_name']
        cur.execute("INSERT INTO facilities (facility_pk, fcode, common_name) VALUES (DEFAULT, '%s', '%s');"%(fcode,common_name))
        conn.commit()
        return redirect(url_for('add_facility'))
    return render_template('login.html')

@app.route('/asset_report', methods=['GET', 'POST'])
#def *():

@app.route('/transfer_report', methods=['GET', 'POST'])
#def *():

@app.route('/dispose_asset', methods=['GET', 'POST'])
#def *():

@app.route('/transfer_req', methods=['GET', 'POST'])
#def *():

@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'GET':
        return render_template('add_asset.html')
    if request.method == 'POST' and ('asset_tag' in request.form and 'description' in request.form):
        asset_tag = request.form['asset_tag']
        description = request.form['description']
        #facilty = request.form['facility']
        cur.execute("INSERT INTO assets (asset_pk, asset_tag, description) VALUES (DEFAULT, '%s', '%s');"%(asset_tag,description))
#        cur.execute("INSERT INTO asset_status (asset_fk, facility_fk, arrival_dt, disposed) SELECT VALUES (
        conn.commit()
        return redirect(url_for('add_asset'))
    return render_template('login.html')

@app.route('/dispose_asset', methods=['GET', 'POST'])
#def *():

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    #session['logged_in'] = FALSE
    return redirect(url_for("login"))

#_/CLIPBOARD\_____________________________
#@app.route('/*', methods=['GET', 'POST'])
#def *():
#_________________________________________

        
# HELPERS #        
def check_username(name):
    SQL = "SELECT * FROM users WHERE username=%s;"
    data = (name,)
    cur.execute(SQL, data)
    user_res = cur.fetchall()
    return bool(user_res)
#

def verify_password(name, string):
    cur.execute("SELECT password FROM users WHERE username = %s;"%(name))
    user_res = cur.fetchone()
    #cur.execute("SELECT password FROM users where user_pk = '%s';"%user_res()
    #user_res = cur.fetchone()
    print(user_res['password'] == string)
    return (user_res['password'] == string)
#

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)
#
