import webpy
from flask import Flask

def handler(app: Flask, *args):
	from flask import request, session

	username, password = \
		request.json.get("username"), request.json.get("password")

	session["username"] = username
	session["password"] = password

	return ""
