from flask import Flask, render_template, request, session
from config import dbname, dbhost, dbport
import psycopg2
import json
import time
from datetime import datetime



#globals
app = Flask(__name__)
app.secret_key = 'c34f5286bed45063'
#conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
#cur = conn.cursor()

# REST FUNCTIONS #

@app.route('/rest')
def rest():
    if request.method == 'GET':
        return render_template('rest.html')
    if request.method == 'POST':
        return render_template('rest.html')
    return render_template('rest.html')

@app.route('/rest/lost_key', methods=['POST'])
def lost_key():
#####################################################################################
# date_converter() and datetime handling impsired from code from:
#   https://code-maven.com/serialize-datetime-object-as-json-in-python
#
    def date_converter(d):
        if isinstance(d, datetime):
            return d.__str__()
    
    dat = dict()
    dat['timestamp'] = datetime.utcnow()
    dat['result'] = 'OK'
    dat['key'] = 'LOST-Df4;5[L15J20fa92jaMd@q]%w#a'
    data = json.dumps(dat, default = date_converter)
    return data

@app.route('/rest/activate_user', methods=['POST'])
def activate_user():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    else:
        redirect('rest')
    
    conn = psycopg2.connect(dbname=dbname,host=dbhost,port=dbport)
    cur  = conn.cursor()
    
    ##if user exists and is inactive ## 
    #SQL="""
    #SELECT user_pk p,active a FROM users u WHERE username un ilike %s 
    #"""

    #SQL="""
    #INSERT INTO TABLE users VALUES ( DEFAULT, %s, 1)
    #"""    
    #cur.execute(SQL, req['username'])

    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['result'] = 'OK'
    data = json.dumps(dat)
    
    conn.close
    return data

    #for queries:
    #req['timestamp']
    #req['username']

@app.route('/rest/suspend_user', methods=["POST"])
def suspend_user():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    else:
        redirect('rest')
    #do queries
    
    conn = psycopg2.connect(dbname=dbname,host=dbhost,port=dbport)
    cur  = conn.cursor()
    
    #SQL="""
    #DELETE FROM TABLE users WHERE username ilike %s
    #"""    
    #cur.execute(SQL, req['username'])
    
    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['result'] = 'OK'
    data = json.dumps(dat)
    
    conn.close()
    return data
    
    #for queries:
    #req['timestamp]'
    #req['username']

######################################################################################
#   list_products()
#   the following is borrowed from dellsworth@github.com/lost/src
#   i dont think im getting the results I hope for here... 
#   i had to remove "sec_" from a couple of parts of SQL to match my table
#   
######################################################################################

@app.route('/rest/list_products', methods=('POST',))
def list_products():
    """This function is huge... much of it should be broken out into other supporting
        functions"""
    
    # Check maybe process as plaintext
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    # Unmatched, take the user somewhere else
    else:
        redirect('rest')
    
    # Setup a connection to the database
    conn = psycopg2.connect(dbname=dbname,host=dbhost,port=dbport)
    cur  = conn.cursor()
    
    # If execution gets here we have request json to work with
    # Do I need to handle compartments in this query?
    if len(req['compartments'])==0:
        print("have not compartment")
        # Just handle vendor and description
        SQLstart = """select vendor,description,string_agg(c.abbrv||':'||l.abbrv,',')
from products p
left join security_tags t on p.product_pk=t.product_fk
left join compartments c on t.compartment_fk=c.compartment_pk
left join levels l on t.level_fk=l.level_pk"""
        if req['vendor']=='' and req['description']=='':
            # No filters, add the group by and query is ready to go
            SQLstart += " group by vendor,description"
            cur.execute(SQLstart)
        else:
            if not req['vendor']=='' and not req['description']=='':
                req['vendor']="%"+req['vendor']+"%"
                req['description']="%"+req['description']+"%"
                SQLstart += " where description ilike %s and vendor ilike %s group by vendor,description"
                cur.execute(SQLstart,(req['description'],req['vendor']))
            elif req['vendor']=='':
                req['description']="%"+req['description']+"%"
                SQLstart += " where description ilike %s group by vendor,description"
                cur.execute(SQLstart,(req['description'],))
            elif req['description']=='':
                req['vendor']="%"+req['vendor']+"%"
                SQLstart += " where vendor ilike %s group by vendor,description"
                cur.execute(SQLstart,(req['vendor'],))
    else:
        print("have compartment %s"%len(req['compartments']))
        # Need to handle compartments too
        SQLstart = """select vendor,description,string_agg(c.abbrv||':'||l.abbrv,',')
from security_tags t
left join compartments c on t.compartment_fk=c.compartment_pk
left join levels l on t.level_fk=l.level_pk
left join products p on t.product_fk=p.product_pk
where product_fk is not NULL and c.abbrv||':'||l.abbrv = ANY(%s)"""
        if req['vendor']=='' and req['description']=='':
            # No filters, add the group by and query is ready to go
            SQLstart += " group by vendor,description,product_fk having count(*)=%s"
            cur.execute(SQLstart,(req['compartments'],len(req['compartments'])))
        else:
            if not req['vendor']=='' and not req['description']=='':
                req['vendor']="%"+req['vendor']+"%"
                req['description']="%"+req['description']+"%"
                SQLstart += " and description ilike %s and vendor ilike %s group by vendor,description,product_fk having count(*)=%s"
                cur.execute(SQLstart,(req['compartments'],req['description'],req['vendor'],len(req['compartments'])))
            elif req['vendor']=='':
                req['description']="%"+req['description']+"%"
                SQLstart += " and description ilike %s group by vendor,description,product_fk having count(*)=%s"
                cur.execute(SQLstart,(req['compartments'],req['description'],len(req['compartments'])))
            elif req['description']=='':
                req['vendor']="%"+req['vendor']+"%"
                SQLstart += " and vendor ilike %s group by vendor,description,product_fk having count(*)=%s"
                cur.execute(SQLstart,(req['compartments'],req['vendor'],len(req['compartments'])))
    
    # One of the 8 cases should've run... process the results
    dbres = cur.fetchall()
    listing = list()
    for row in dbres:
        e = dict()
        e['vendor'] = row[0]
        e['description'] = row[1]
        if row[2] is None:
            e['compartments'] = list()
        else:
            e['compartments'] = row[2].split(',')
        listing.append(e)
    
    # Prepare the response
    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['listing'] = listing
    data = json.dumps(dat)

    conn.close()
    return data

"""
@app.route('/rest/list_products', methods=["POST"])
def list_products():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    #do queries
    conn = psycopg2.connect(dbname=dbname, host=dbhost, port=dbport)
    cur = conn.cursor()
    #no compartment
    SQL = 
    SELECT vendor,description FROM products p
    
    if True:  
        req['vendor']="%"+req['vendor']+"%"
        req['description']="%"+req['description']+"%"
        SQL += "WHERE description ilike %s and vendor ilike %s group by vendor,description"
        cur.execute(SQL,(req['description'],req['vendor']))

    dbres = cur.fetchall()
    listing = list()
    for row in dbres:
        e = dict()
        e['vendor'] = row[0]
        e['description'] = row[1]
        listing.append(e)

    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['listing'] = listing
    
    #listing['vendor'] = req['vendor']
    #listing['description'] = req['description']
    #listing['compartments'] = req['compartments']
    
    data = json.dumps(dat)
    conn.close()
    return data
    
    #for queries:
    #req['timestamp']
    #req['vendor']
    #req['description']
    #req['compartments']
"""

@app.route('/rest/add_products', methods=["POST"])
def add_products():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    else:
        redirect('rest')

    #do queries
    
    conn = psycopg2.connect(dbname=dbname,host=dbhost,port=dbport)
    cur  = conn.cursor()
    
    #SQL="""
    #INSERT INTO TABLE products VALUES ( DEFAULT, %s, %s, %s, %s)
    #"""    
    #cur.execute(SQL, req['vendor'], req['description'], req['alt_description'], req['compartments'])


    dat = dict()
    dat['timestamp'] = req['timestamp']
    dat['result'] = 'OK'
    data = json.dumps(dat)
    
    conn.close()
    return data

    #for queries: req['new_products']
    #req['timestamp']
    #req['new_products']['vendor']
    #req['new_products']['description']
    #req['new_products']['alt_description']
    #req['new_products']['compartments']


@app.route('/rest/add_asset', methods=["POST"])
def add_asset():
    if request.method=='POST' and 'arguments' in request.form:
        req=json.loads(request.form['arguments'])
    else:
        redirect('rest')

    conn = psycopg2.connect(dbname=dbname,host=dbhost,port=dbport)
    cur  = conn.cursor()
    
    #SQL="""
    #INSERT INTO TABLE assets VALUES ( DEFAULT, %s, %s, %s, %s)
    #"""    
    #cur.execute(SQL, req['vendor'], req['description'], req['alt_description'], req['facility'])
    
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
    return render_template('filter.html')

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

    SQL = "SELECT request_id , asset_tag FROM assets a JOIN asset_on ao ON a.asset_pk = ao.asset_fk JOIN convoys c ON ao.convoy_fk=c.convoy_pk WHERE (ao.load_dt < now() and (aa.unload_dt is NULL or aa.unload_ft > %s)) or (WHERE source_fk = (SELECT facility_pk FROM facilities WHERE fcode = %s) or WHERE dest_fk = (SELECT facility_pk FROM facilities WHERE fcode = %s));"
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
