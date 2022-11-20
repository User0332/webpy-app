import webpy
from flask import Flask, session, redirect

def handler(app: Flask, *args):
	if not session.get("username"):
		return redirect('/')

	document = webpy.documentify("dashboard.html")

	return document._stringify()
