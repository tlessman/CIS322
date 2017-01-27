from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/filter')
def filter():
    return render_template('filter.html')

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
