#!/usr/bin/env python
# coding:utf-8
from flask import Flask,request
import requests,json

app=Flask(__name__)

@app.route('/')
def hello_world():
	return 'hello world'

@app.route('/api')
def api():
	return request.get_data() 
	# return json.dumps(jsondata)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8000)