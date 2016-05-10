#!/usr/bin/env python
# coding:utf-8
from flask import Flask,render_template
from flask.ext.script import Manager
from moduleClass import User

app=Flask(__name__)
m=Manager(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def get_user(name):
	if not name:
		name='world'
	return render_template('user.html',name=name)

@app.route('/u')
def user_index():
	user=User(1,'fengye')
	return render_template('user_index.html',user=user)	

@app.route('/uid/<uid>')
def query_user(uid):
	user=None
	if int(user_id) == 1:
		user=User(1,'fengye')

	return render_template('user_id.html',user=user)

@app.route('/users')
def user_list():
	users=[]
	for i in xrange(1, 11):
		user=User(i,'fengye'+str(i))
		users.append(user)

	return render_template("users.html",users=users)

@app.route('/one')
def one():
	return render_template('one_base.html')

@app.route('/two')
def two():
	return render_template('two_base.html')

@app.route('/info')
def get_info():
	flash("hello fengye")
	return render_template('index.html')

if __name__ == '__main__':
	m.run()