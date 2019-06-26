from flask import Flask, url_for, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('account'))
    return render_template('login.html', error=error)
