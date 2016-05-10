#!/usr/bin/env python
# coding:utf-8
from flask import abort,request,flash,Flask,render_template
from flask.ext.script import Manager

app=Flask(__name__)
app.secret_key='123'
m=Manager(app)


@app.route('/')
def index():
	return render_template('index.html')

#提示消息
@app.route('/info')
def hello_world():
	flash("hello fengye")
	return render_template('info.html')

@app.route('/login',methods=['POST'])
def login():
	form=request.form
	username=form.get('username')
	password=form.get('password')
	if not username:
		flash("please input username")
		return render_template('info.html')
	if not password:
		flash("please input password")
		return render_template('info.html')
	if username=='fengye' and password=='123456':
		flash("login success")
		return render_template('info.html')
	else:
		flash('username or password is error')
		return render_template('info.html')

@app.errorhandler(404)
def not_find(e):
	return render_template('404.html')

app.route('/user/<name>')
def get_user(name):
	if name =='lpc':
		return render_template('user.html',name=name)
	else:
		abort(404)
	
if __name__ == '__main__':
	m.run()