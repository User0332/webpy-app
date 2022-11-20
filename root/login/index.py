import webpy
from flask import Flask, request, session

def handler(app: Flask, *args):
	username, password = \
		request.json.get("username"), request.json.get("password")

	session["username"] = username
	session["password"] = password

	return ""
