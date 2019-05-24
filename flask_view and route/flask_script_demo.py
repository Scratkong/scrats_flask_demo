from flask import Flask
# need to install flask-script before import
from flask_script import Manager

app = Flask(__name__)

# 把Manager类与应用程序实力进行关联
manager = Manager(app)

@app.route('/')
def index():
    return 'hello flask-script'

if __name__ == '__main__':
    manager.run()

# use ' python flask_script_demo.py runserver  in terminal to run the server