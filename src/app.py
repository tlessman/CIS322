from flask import Flask, render_template, request
#from config import dbname, dbhost, dbport

app = Flask(__name__)
"""
@app.route('/')
def index():
    return render_template('index.html')
"""
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/filter')
def filter():
    if request.method == 'GET' and 'username' in request.args:
        return render_template('filter.html', data=request.args.get('username'))
    if request.method == 'POST' and 'username' in request.form:
        return render_template('filter.html', data=request.form['username'])
    return render_template('login.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/transit')
def transit():
    return render_template('transit.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)
