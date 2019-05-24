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

if __name__=="__main__":
    app.run()