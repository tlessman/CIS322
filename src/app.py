from flask import Flask, render_template, request, session
from config import dbname, dbhost, dbport
import psycopg2



#globals
app = Flask(__name__)
app.secret_key = 'c34f5286bed45063'
conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
cur = conn.cursor()



@app.route('/')
def login():
    return render_template('login.html', dbname=dbname, dbhost=dbhost, dbport=dbport)

@app.route('/filter')
def filter():
    if request.method == 'GET' and 'username' in request.args:
        return render_template('filter.html', data=request.args.get('username'))
    if request.method == 'POST' and 'username' in request.form:
        return render_template('filter.html', data=request.form['username'])
    return render_template('login.html')
SQL = "SELECT * FROM assets WHERE asset_pk = %s"
data = (1,)
cur.execute(SQL, data)
result = cur.fetchall()
session['res_asset'] = result

@app.route('/inventory')
def inventory():
    if request.method == 'GET' and (('sel_date' in request.args and 'sel_facility' in request.args) or ('sel_date' in request.args or 'sel_facility' in request.args)):
        return render_template('inventory.html', data1=request.args.get('sel_date'), data2=request.args.get('sel_facility'))
    if request.method == 'POST' and ('sel_date' in request.form and 'sel_facility' in request.form):
        return render_template('inventory.html', data1=request.form['sel_date'], data2=request.form['sel_facility'])
    if request.methon == 'POST' and ('sel_date' in request.form or 'sel_facility' in request.form):
        return render_template('inventory.html', data1=request.form['sel_date'], data2=request.form['sel_facility'])
    return render_template('inventory.html')

@app.route('/transit')
def transit():
    if request.method == 'GET' and (('sel_date' in request.args and 'sel_facility' in request.args) or ('sel_date' in request.args or 'sel_facility' in request.args)):
        return render_template('transit.html', data1=request.args.get('sel_date'), data2=request.args.get('sel_facility'))
    if request.method == 'POST' and (('sel_date' in request.form and 'sel_facility' in request.form) or ('sel_date' in request.form or 'sel_facility' in request.form)):
        return render_template('transit.html', data1=request.form['sel_date'], data2=request.form['sel_facility'])
    return render_template('transit.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)
