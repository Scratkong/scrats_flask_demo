from flask import Flask, request, jsonify, redirect, url_for
from werkzeug.routing import BaseConverter

# 自定义转换器 ， 限制用户访问规则
# BaseConverter 转换器基类
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        # 接受第一个参数当匹配规则进行保存
        self.regex = args[0]


class Config(object):
    DEBUG = True

# 创建flask类对象，指向程序所在的包的名称
app = Flask(__name__)

# 添加自定义转换器到转换器字典中，制定转换器使用时名字为：re
# app.url_map.converters['regex'] = RegexConverter
app.url_map.converters['re'] = RegexConverter


@app.route('/user/<re("[0-9]{3}"):user_id>')
def user_info(user_id):
    return 'user_id is %s '%user_id


# 从配置对象中加载配置（常用)
# app.config.from_object(Config)

# 从配置文件中加载配置
app.config.from_pyfile('config.ini')

# 使用代码加载相关配置
app.config.from_envvar('FLASKCONFIG')


@app.route('/')
def index():
    return 'Hello world'

@app.route('/demo1')
def demo1():
    return 'demo1'

# @app.route('/user/<user_id>')
# def user_info(user_id):
#     return 'hello %s'% user_id

# @app.route('/user/<int:user_id>')
# def user_info(user_id):
#     return 'hello %d'%user_id

@app.route('/demo2', methods=['GET', 'POST'])
def demo2():
    return request.method

@app.route('/demo4')
def demo4():
    json_dict = {
        'user_id': 10,
        'user_name': 'scrat'
    }
    return jsonify(json_dict)

@app.route('/demo5')
def demo5():
    # return redirect('http://www.baidu.com')
    # return redirect(url_for('demo1'))
    return redirect(url_for('user_info', user_id=100))

@app.route('/demo6')
def demo6():
    return '状态码为 666', 666

@app.errorhandler(500)
def internal_server_error(e):
    return '服务器搬家了'

# 捕获制定异常
@app.errorhandler(ZeroDivisionError)
def zero_division_error(e):
    return '除数不能为0'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

