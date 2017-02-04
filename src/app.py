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

@app.route('/dev')
def dev():
    if request.method == 'GET' and 'search' in request.args:
        return render_template('dev.html', data=request.args.get('search'))
    if request.method == 'POST' and 'search' in request.form:
        return render_template('dev.html', data=request.form('search'))
    SQL = "%s"
    data = (1,)
    cur.execute(SQL, data)
    result - cur.fetchall()
    session['res_dev'] = result
    data_report = []
    for r in result:
        e= dict()
        e['pk']=r[0]
        data_report.append(e)
    session['data_report'] = data_report

    return render_template('dev.html')

@app.route('/inventory')
def inventory():
    #SQL = "SELECT * FROM assets WHERE asset_pk = %s"
    #data = (1,)
    #cur.execute(SQL, data1)
    #result = cur.fetchall()
    #session['res_asset'] = result

    if request.method == 'GET' and (('sel_date' in request.args and 'sel_facility' in request.args) or ('sel_date' in request.args or 'sel_facility' in request.args)):
        return render_template('inventory.html', data1=request.args.get('sel_date'), data2=request.args.get('sel_facility'))
    if request.method == 'POST' and ('sel_date' in request.form and 'sel_facility' in request.form):
        return render_template('inventory.html', data1=request.form['sel_date'], data2=request.form['sel_facility'])
    if request.methon == 'POST' and ('sel_date' in request.form or 'sel_facility' in request.form):
        return render_template('inventory.html', data1=request.form['sel_date'], data2=request.form['sel_facility'])
    return render_template('inventory.html')

@app.route('/transit')
def transit():

    #SQL = "SELECT request_id, asset_tag FROM assets a JOIN asset_on ao ON a.asset_pk = %s JOIN convoys c ON ao.convoy_fk=c.convoy_pk WHERE ao.load_dt < now() and (aa.unload_dt is NULL or aa.unload_ft > %s)"
    #data = (1,2,)
    #cur.execute(SQL, data2, data1)
    #result = cur.fetchall()
    #session['res_transit'] = result

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
