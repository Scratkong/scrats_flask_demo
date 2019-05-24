from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome '


# 设置cookie
@app.route('/cookie')
def set_cookie():
    resp = make_response('this is to set cookie')
    resp.set_cookie('username','scratkong')
    return resp

# 获取cookie
@app.route('/request')
def resp_cookie():
    resp = request.cookies.get('username')
    return resp

if __name__ == "__main__":
    app.run()