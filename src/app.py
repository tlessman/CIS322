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
from jinja2 import Template
import psycopg2
import json
import datetime

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
    print("got to activate user")
    if request.method =='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    else:
        return redirect(url_for('rest'))
    ##if user exists, do:
    if user_available(req['username']) == False:
        print("in user exists")
        cur.execute( "SELECT * FROM users WHERE username ~~* %s;", (req['username'],) )
        res = cur.fetchall()
        cur.execute('UPDATE users SET active = TRUE, password = %s WHERE username = %s;', (req['password'], req['username']) )
        conn.commit()
        dat = dict()
        dat['timestamp'] = req['timestamp']
        dat['result'] = 'USER ACTIVE AND PASSWORD UPDATED'
        data = json.dumps(dat)
        return data
    ##else create user
    else:
        print("in new user")
        cur.execute("INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, '%s', '%s', '%s', TRUE);"%(req['username'],req['password'],req['role']))
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
        cur.execute('SELECT * FROM users WHERE (username ~~* %s and active ==1);',(req['username'],))
        res = cur.fetchone()
        cur.execute('UPDATE users SET active = FALSE WHERE username == %s;',(req['username'],))
        conn.commit()
        dat = dict()
        dat['timestamp'] = req['timestamp']
        dat['result'] = 'USER SUSPENDED'
        data = json.dumps(dat)
        return 'USER SUSPENDED'
    return 'UNSUCCESSFUL'

# PATHS #
@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    session['username'] = ""
    session['role'] = ""
    if 'msg' not in session:
        session['msg'] = ""
    print('pre-log')
    if request.method =='GET':
        print('get')
        return render_template('login.html')    
    if request.method =='POST' and ('username' in request.form and 'password' in request.form):
        print('post')
        name = request.form['username']
        pswd = request.form['password']
        print(name+" "+pswd)
        if user_available(name) == True:
            session['msg'] = "Username does not exist."
            return redirect(url_for('login'))
        cur.execute("SELECT password FROM users WHERE (username = %s);",(name,))
        res = cur.fetchone() 
        print(res)
        print(pswd)
        pres = res[0]
        print(pres)
        if pres == pswd: 
            cur.execute("SELECT active FROM users WHERE username = %s;",(name,))
            res = cur.fetchone()
            print(res)
            sres = res[0]
            if sres == False:
                session['msg'] = "User not authorized."
                return redirect(url_for('login'))
            session['logged_in'] = True   
            session['username'] = name
            cur.execute("SELECT role FROM users WHERE username = '%s';"%(name))
            res = cur.fetchone()
            rres = res[0]
            session['role'] = rres
            session['msg'] = ''
            return redirect(url_for('dashboard'))
        session['msg'] = "Invalid password."
        return redirect(url_for('login'))           
    return render_template('login.html', dbname=dbname, dbhost=dbhost, dbport=dbport)
#

@app.route('/create_user', methods=['GET','POST'])
def create_user():
    return redirect(url_for('rest'))    
#    if request.method == 'GET':
#        session['msg'] = ''
#        return render_template('create_user.html')
#    if request.method == 'POST' and ('username' in request.form and 'password' in request.form):  
#        name = request.form['username']
#        pswd = request.form['password']
#        cur.execute("SELECT 1 FROM users WHERE username = '%s';"%(name))
#        res = cur.fetchone()
#        if res == 1:
#            session['msg'] = "Username taken."
#            return redirect(url_for('create_user'))
#       name = request.form['username']
#        pswd = request.form['password']
#        role = request.form['role']
#        session['msg'] = "Created a new user."
#        cur.execute("INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, '%s', '%s', '%s', TRUE);"%(name,pswd,role))
#        conn.commit() 
#        return redirect(url_for('create_user')) 
#        #
#    #
##    return render_template('create_user.html')
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
    if 'logged_in' not in session:
        session['msg'] = "Unauthorized access."
        return render_template('login.html')
    return render_template('dashboard.html')

@app.route('/add_facility', methods=['GET','POST'])
def add_facility():
    if request.method == 'GET':
        session['msg'] = ''
        return render_template('add_facility.html')
    if request.method == 'POST' and ('fcode' in request.form and 'common_name' in request.form):
        #SQL
        fcode = request.form['fcode']
        common_name = request.form['common_name']
        cur.execute("INSERT INTO facilities (facility_pk, fcode, common_name) VALUES (DEFAULT, '%s', '%s');"%(fcode,common_name))
        conn.commit()
        session['msg'] = 'Facility Added'
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/asset_report', methods=['GET', 'POST'])
def asset_report():
    if request.method == 'GET':
        return render_template('asset_report.html')
    if request.method == 'POST':
        return redirect(url_for('asset_report'))
    return render_template('asset_report.html.html')

#@app.route('/transfer_report', methods=['GET', 'POST'])
#def *():

@app.route('/dispose_asset', methods=['GET', 'POST'])
def dispose_asset():
    if request.method == 'GET':
        if session.get('role') != 0:
            session['msg'] = 'Asset disposal only available to Logistics Officers'
            return redirect(url_for('dashboard'))
        session['msg'] = ''
        return render_template('dispose_asset.html')
    if request.method == 'POST' and 'asset_tag' in request.form: #and session['role'] == 0:
        tag = request.form['asset_tag']
        timestamp = datetime.datetime.utcnow().isoformat()
        cur.execute("SELECT asset_pk FROM assets WHERE asset_tag = %s",(tag,))
        res = cur.fetchone()
        ares = res[0]
        cur.execute("UPDATE asset_at SET disposed = %s, disposed_dt = %s WHERE asset_fk = %s;", (True, timestamp, ares))
        conn.commit()
        session['msg'] = 'Asset Disposed'
        return redirect(url_for('dashboard'))
    return render_template('login.html')
    #   
@app.route('/transfer_req', methods=['GET', 'POST'])
def transfer_req():
    if request.method == 'GET':
        if session.get('role') != 0:
            session['msg'] = 'Transfer Request only available to Logistics Users'
            return redirect(url_for('dashboard'))
        session['msg'] = ''
        return render_template('transfer_req.html')
    if request.method == 'POST':
        return redirect(url_for('transfer_req'))
    return render_template('transfer_req.html')

@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'GET':
        session['msg'] = ''
        cur.execute("SELECT fcode FROM facilities;")
        res = cur.fetchall()
        session['fcodes'] = res
        cur.execute("SELECT common_name FROM facilities;")
        res = cur.fetchall()
        session['facilities'] = res
        return render_template('add_asset.html')
    if request.method == 'POST' and ('asset_tag' in request.form and 'description' in request.form):
        asset_tag = request.form['asset_tag']
        description = request.form['description']
        facility = request.form['facility']
        timestamp = datetime.datetime.utcnow().isoformat()
        cur.execute("INSERT INTO assets (asset_pk, asset_tag, description) VALUES (DEFAULT, '%s', '%s');"%(asset_tag,description))
        conn.commit()
        cur.execute("SELECT asset_pk FROM assets WHERE asset_tag = %s;", (asset_tag,))
        res = cur.fetchone()
        ares = res[0]
        cur.execute("SELECT facility_pk FROM facilities WHERE fcode = %s;", (facility,))
        res = cur.fetchone()
        fres = res[0]
        cur.execute("INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed) VALUES (%s, %s, %s, %s);", (ares, fres, timestamp, False))
        conn.commit()
        session['msg'] = 'Asset Added'
        return redirect(url_for('dashboard'))
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
def user_available(name):
    cur.execute("SELECT * FROM users WHERE username = %s;", (name,) )
    user_res = cur.fetchone()
    if user_res is None:
        return True
    else:
        return False
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
