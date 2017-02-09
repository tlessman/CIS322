from flask import Flask, render_template, request, session
from config import dbname, dbhost, dbport
import psycopg2



#globals
app = Flask(__name__)
app.secret_key = 'c34f5286bed45063'
conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
cur = conn.cursor()

# REST FUNCTIONS #

@app.route('/rest')

@app.route('/rest/lost_key', methods=['POST'])
def losy_key():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['result'] = 'OK'
    dat['lost_key'] = 'LOST-Df4;5[L15J20fa92jaMd@q]%w#a'
    data = json.dumps(dat)
    return data

@app.route('/rest/activate_user', methods=['POST'])
def activate_user():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    #do queries
    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['result'] = 'OK'
    data = json.dumps(dat)
    return data

    #for queries:
    #req['timestamp']
    #req['username']

@app.route('/rest/suspend_user', methods=["POST"])
def suspend_user():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    #do queries
    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['result'] = 'OK'
    data = json.dumps(dat)
    return data
    
    #for queries:
    #req['timestamp]'
    #req['username']


@app.route('/rest/list_products')
def list_products():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    #do queries
    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['listing'] = dict()
    #listing
    dat['listing']['vendor'] = req['vendor']
    dat['listing']['description'] = req['description']
    dat['listing']['compartments'] = req['compartments']
    data = json.dumps(dat)
    return data
    
    #for queries:
    #req['timestamp']
    #req['vendor']
    #req['description']
    #req['compartments']


@app.route('/rest/add_products')
def add_products():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    #do queries
    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['result'] = 'OK'
    data = json.dumps(dat)
    return data

    #for queries: req['new_products']
    #req['timestamp']
    #req['new_products']['vendor']
    #req['new_products']['description']
    #req['new_products']['alt_description']
    #req['new_products']['compartments']
    

@app.route('/rest/add_asset')
def add_asset():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['result'] = 'OK'
    data = json.dumps(dat)
    return data

    #for queries:
    #req['timestamp']
    #req['vendor']
    #req['description']
    #req['compartments']
    #req['facility']
    

# HTML ROUTING #

@app.route('/')
def login():
    return render_template('login.html', dbname=dbname, dbhost=dbhost, dbport=dbport)

@app.route('/filter', methods=["POST"])
def filter():
    if request.method == 'GET' and 'username' in request.args:
        return render_template('filter.html', data=request.args.get('username'))
    if request.method == 'POST' and 'username' in request.form:
        return render_template('filter.html', data=request.form['username'])
    return render_template('login.html')

@app.route('/dev', methods=["POST"])
def dev():
    if request.method == 'GET' and 'search' in request.args:
        return render_template('dev.html', data=request.args.get('search'))
    if request.method == 'POST' and 'search' in request.form:
        return render_template('dev.html', data=request.form('search'))
    SQL = "SELECT %s FROM assets;"
    data = (1,)
    cur.execute(SQL, data)
    result - cur.fetchall()
    session['res_dev'] = result
    data_report = []
    for r in res_dev:
        e= dict()
        e['pk']=r[0]
        data_report.append(e)
    session['data_report'] = data_report

    return render_template('dev.html')

@app.route('/inventory', methods=["POST"])
def inventory():
    #SQL = "SELECT asset_tag, common_name, arrive_dt FROM assets a JOIN asset_at aa ON a.asset_pk = aa.asset_fk JOIN convoys c ON ao.convoy_fk=c.convoy_pk WHERE ao.load_dt < now() and (aa.unload_dt is NULL or aa.unload_ft > %s) or (WHERE source_fk = (SELECT facility_pk FROM facilities WHERE fcode = %s) or WHERE dest_fk = (SELECT facility_pk FROM facilities WHERE fcode = %s));"
    SQL = "SELECT * FROM assets;"

    #data = (1,)
    #cur.execute(SQL, data1, data2, data2)
    
    cur.execute(SQL)
    result = cur.fetchall()
    session['res_asset'] = result

    if request.method == 'GET' and (('sel_date' in request.args and 'sel_facility' in request.args) or ('sel_date' in request.args or 'sel_facility' in request.args)):
        return render_template('inventory.html', data1=request.args.get('sel_date'), data2=request.args.get('sel_facility'))
    if request.method == 'POST' and ('sel_date' in request.form and 'sel_facility' in request.form):
        return render_template('inventory.html', data1=request.form['sel_date'], data2=request.form['sel_facility'])
    if request.methon == 'POST' and ('sel_date' in request.form or 'sel_facility' in request.form):
        return render_template('inventory.html', data1=request.form['sel_date'], data2=request.form['sel_facility'])
    return render_template('inventory.html')

@app.route('/transit', methods=["POST"])
def transit():

    SQL = "SELECT request_id, asset_tag FROM assets a JOIN asset_on ao ON a.asset_pk = ao.asset_fk JOIN convoys c ON ao.convoy_fk=c.convoy_pk WHERE (ao.load_dt < now() and (aa.unload_dt is NULL or aa.unload_ft > %s)) or (WHERE source_fk = (SELECT facility_pk FROM facilities WHERE fcode = %s) or WHERE dest_fk = (SELECT facility_pk FROM facilities WHERE fcode = %s));"
    data = (1,2,)
    cur.execute(SQL, data1, data2, data2)
    result = cur.fetchall()
    session['res_transit'] = result

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
