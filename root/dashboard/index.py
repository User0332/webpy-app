import webpy
from flask import Flask

def handler(app: Flask, *args):
	from flask import session, redirect
	
	if not session.get("username"):
		return redirect('/')

	document = webpy.documentify("dashboard.html")

	return document._stringify()
