#!/usr/bin/env python
#encoding=utf-8
from flask import Flask,request,url_for
app=Flask(__name__)

@app.route('/')
def index():
	return "<h1>hello index</h1>"

# 指定参数
@app.route('/user/<name>')
def user(name):
	return '<h1>hello %s !</h1>' %name

@app.route('/method',methods=['POST'])
def hello_method():
	return 'hello method'

@app.route('/query')
def hello_query():
	id=request.args.get('id')
	return 'hello query:%s' %id

@app.route('/query_url')
def query_url():
	return 'query_url:'+url_for(query)

if __name__ == '__main__':
	# app.run(host='0.0.0.0',port=8000,debug=True)
	app.run(debug=True)