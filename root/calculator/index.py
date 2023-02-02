import webpy
from flask import Flask

def handler(app: Flask, *args):
	from flask import render_template, session, redirect

	if not session.get("username"): return redirect('/')
	
	document = webpy.documentify("calculator.html")

	return document._stringify()