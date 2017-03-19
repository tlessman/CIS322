"""SELECT asset_tag,username,request_dt,approved_dt,load_dt, unload_dt 
FROM assets a 
    JOIN asset_at at ON (a.asset_pk = at.asset_fk) 
    JOIN facilities f ON (f.facility_pk = at.facility_fk) 
    JOIN users u ON (u.user_pk = req_user_fk)
    JOIN users u ON (u.user_pk = app_user_fk)
    JOIN transit t ON (f.facility_pk = t.src_fk)
    JOIN transit t ON (f.facility_pk = t.dest_fk)
WHERE disposed = FALSE;"""

from flask import Flask, render_template, request, session, redirect, url_for
from config import dbname, dbhost, dbport
import psycopg2
import json
from datetime import datetime

# GLOBALS #
app = Flask(__name__)
app.secret_key='c34f5286bed45063'
#dbname = 'lost' 
#dbhost = '127.0.0.1'
#dbport = 5432
conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
cur = conn.cursor()

# REST FUNCTIONS #
@app.route('/rest')
def rest():
    if request.method == 'GET':
        return render_template('rest.html')
    if request.method == 'POST':
        return render_template('rest.html')
    return render_tempate('rest.html')

@app.route('/rest/activate_user', methods=['POST'])
def activate_user():
    if request.method =='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    else:
        return redirect(url_for('rest'))
    ##if user exists, do:
    if user_available(req['username']) == False:
        cur.execute('SELECT * FROM users WHERE username ~~* %s;'%(req['username']))
        res = cur.fetchall()
    if res[user_pk]:
        cur.execute('UPDATE users SET active = TRUE, password = %s WHERE username == %s;'%(req['password'], req['username']))
        conn.commit()
        dat = dict()
        dat['timestamp'] = req['timestamp']
        dat['result'] = 'USER ACTIVE AND PASSWORD UPDATED'
        data = json.dumps(dat)
        return data
    ##else create user
    else:
       cur.execute("INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, '%s', '%s', '%s', TRUE);"%(username,password,role))
       conn.commit()
       dat = dict()
       dat['timestamp'] = req['timestamp']
       dat['result'] = 'USER CREATED'
       data = json.dumps(dat)
       return data 
        

@app.route('/rest/suspend_user', methods=['POST'])
def suspend_user():
    if request.method =='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    else:
        return redirect(url_for('rest'))
    ##if user exists and is active, do:
        cur.execute('SELECT * FROM users WHERE (username ~~* %s and active ==1;'%(req['username']))
        res = cur.fetchall()
    if res[user_pk]:
        cur.execute('UPDATE users SET active = FALSE WHERE username == %s;'%(req['username']))
        conn.commit()
        dat = dict()
        dat['timestamp'] = req['timestamp']
        dat['result'] = 'OK'
        data = json.dumps(dat)
        return data

# PATHS #
@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    session['msg'] = ""
    
    session['username'] = ""
    session['role'] = ""
    print('pre-log')
    if request.method =='GET':
        print('get')
        return render_template('login.html')    
    if request.method =='POST' and ('username' in request.form and 'password' in request.form):
        print('post')
        name = request.form['username']
        pswd = request.form['password']
        print(name+" "+pswd)
        #cur.execute("SELECT 1 FROM users WHERE username = '%s';"%(name))
        #ures = cur.fetchone()
        #if ures != 1:
        #    session['msg'] = "Username does not exist."
        #    return redirect(url_for('login'))
        #cur.execute("SELECT 1 FROM users WHERE username = '%s', password = '%s';"%(name, pswd))
        #pres = cur.fetchone()
        #if pres['password'] != 1:
        #    session['msg'] = "Invalid Password."
        #    return redirect(url_for('login'))
        session['logged_in'] = True   
        session['username'] = name
        cur.execute("SELECT role FROM users WHERE username = '%s';"%(name))
        rres = cur.fetchone()
        session['role'] = rres
        return render_template('dashboard.html')
    return render_template('login.html', dbname=dbname, dbhost=dbhost, dbport=dbport)
#

@app.route('/create_user', methods=['GET','POST'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')
    if request.method == 'POST' and ('username' in request.form and 'password' in request.form):  
        #name = request.form['username']
        #pswd = request.form['password']
        #cur.execute("SELECT 1 FROM users WHERE username = '%s';"%(name))
        #res = cur.fetchone()
        #if res == 1:
        #    session['msg'] = "Username taken."
        #    return redirect(url_for('create_user'))
        name = request.form['username']
        pswd = request.form['password']
        role = request.form['role']
        session['msg'] = "Created a new user."
        cur.execute("INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, '%s', '%s', '%s', TRUE);"%(name,pswd,role))
        conn.commit() 
        return redirect(url_for('create_user')) 
           
        #
    #
    return render_template('create_user.html')
#

#@app.route('/username_taken', methods = ['GET', 'POST'])
#def username_taken():
#    if request.method == 'POST' and ('username' in request.form and 'password' in request.form):
#        if check_username(request.form['username']): 
#             return redirect(url_for('create_user'))
#       #
#   #
#   return render_template('create_user.html')
#

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'logged_in' in session:
        return render_template('dashboard.html')
    elif 'logged_in' not in session:
        session['msg'] = "Unauthorized access."
        return render_template('login.html')
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

#@app.route('/asset_report', methods=['GET', 'POST'])
#def *():

#@app.route('/transfer_report', methods=['GET', 'POST'])
#def *():

@app.route('/dispose_asset', methods=['GET', 'POST'])
def dispose_asset():
    if request.method == 'GET':
        return render_template('dispose_asset.html')
    if request.method == 'POST' and 'asset_tag' in request.form: #and session['role'] == 0:
        session['msg'] = ""
        tag = request.form['asset_tag']
        cur.execute("UPDATE assets SET disposed = 1 WHERE asset_tag = '%s';"%(tag))
        conn.commit()
        return redirect(url_for('dashboard'))
    #   
@app.route('/transfer_req', methods=['GET', 'POST'])
#def *():

@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'GET':
        return render_template('add_asset.html')
    if request.method == 'POST' and ('asset_tag' in request.form and 'description' in request.form):
        asset_tag = request.form['asset_tag']
        description = request.form['description']
        facilty = request.form['facility']
        cur.execute("INSERT INTO assets (asset_pk, asset_tag, description) VALUES (DEFAULT, '%s', '%s');"%(asset_tag,description))
        cur.execute("INSERT INTO asset_at ("%())
        conn.commit()
        return redirect(url_for('add_asset'))
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for("login"))

#_/CLIPBOARD\_____________________________
#@app.route('/*', methods=['GET', 'POST'])
#def *():
#_________________________________________

        
# HELPERS #        
#def user_available(name):
#    cur.execute("SELECT count(*) FROM users WHERE username = %s;"%(name))
#    user_res = cur.fetchone()[0]
#    if user_res != 0:
#        return False
##
#
#def verify_login(name, string):
#    cur.execute("SELECT count(*) FROM users WHERE username = %s and password = %s;"%(name,string))
#    user_res = cur.fetchone()[0]
#    if user_res != 1:
#        return False
##

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)
#
