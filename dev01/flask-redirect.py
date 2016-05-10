#!/usr/bin/env python
#encoding=utf-8
from flask import Flask,request,render_template,redirect
app=Flask(__name__)

#访问重定向
@app.route('/')
def index():
	return redirect("http://www.baidu.com")

#异常处理
@app.route("/user/<id>")
def get_userid(id):
	abort(404)


if __name__ == '__main__':
	app.run(debug=True)