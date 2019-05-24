from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mystr = 'hello flask'
    myint = 996
    my_array = [1,2,3,4,5,6]
    my_dict = {
        'name':'scratkong',
        'age': 18
    }
    return render_template('templates_demo.html',
                           my_str=mystr,
                           my_int = myint,
                           my_array = my_array,
                           my_dict = my_dict
                           )
# 自定义过滤器方式一： 添加列表反转的过滤器
def do_listreverse(li):
    # 通过原列表创建一个新列表
    temp_li = list(li)
    # 将新列表进行反转
    temp_li.reverse()
    return temp_li

app.add_template_filter(do_listreverse,'lireverse')

#自定义过滤器方式二：装饰器
@app.template_filter('lireverse')
def do_listreverser(li):
    # 通过源列表创建一个新列表
    temp_li = list(li)
    # 将列表进行反转
    temp_li.reverse()
    return temp_li


if __name__=="__main__":
    app.run()