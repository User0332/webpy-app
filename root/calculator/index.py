from flask import Flask, render_template, session, redirect

def handler(app: Flask, *args):
	if not session.get("username"): return redirect('/')
	
	return render_template("calculator.html")