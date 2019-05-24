from flask import Flask, session, redirect, url_for

app = Flask(__name__)

@app.route('/index')
def index1():
    session['username'] = 'scrat'
    return redirect(url_for('index'))

@app.route('/')
def index():
    return session.get('username')

if __name__ == '__main__':
    app.run()