from flask import Flask,render_template
import datetime

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return '您好啊！'

@app.route("/user/<name>")
def welcome(name):
    return "你好，%s"%name

@app.route("/user/<int:id>")
def welcom2(id):
    return "你好,%d 号的会员"%id

@app.route("/")
def index2():
    time = datetime.date.today()
    name = ["小张", "小五", "小赵"]
    task = {"任务": "打扫卫生", "时间": "3小时"}
    return render_template("index.html", var=time, list=name, task=task)


# 表单提交
# @app.route("test/register")
# def register():
#     return render_template("test/register.html")
#
# @app.route('/result',methods=['POST','GET'])
# def register():
#     return render_template("test/result.html")





if __name__ == '__main__':
    app.run(debug=True)
