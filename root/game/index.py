from pysite.tags import *
from flask import Flask

def handler(app: Flask, *args):
	from flask import session, redirect

	if not session.get("username"): return redirect('/')

	# this can be done much easier (and without JS) using jinja templating,
	# but the PyX attribute templating is used to display the username here
	# in the heading as an example of PyX integration with WebPy
	username = session.get("username")

	return (
		html(data='\n\t\t', children=[html(data='\n\t\t\t', children=[head(data='\n\t\t\t\t', children=[script( children=[], **{'src': '../static/js/game.js','defer': ""}),link( children=[], **{'rel': 'stylesheet','href': '../static/css/theme.css'}),link( children=[], **{'rel': 'stylesheet','href': '../static/css/game.css'}),title(data='Game', children=[], **{})], **{}),body(data='\n\t\t\t\t', children=[h1( children=[], **{'id': 'gametitle','name': username}),canvas(data='\n\t\t\t\t\t\t', children=[img( children=[], **{'id': 'player','src': '../static/images/player.png'})], **{'id': 'gamearea'})], **{'class': 'page-center','style': 'overflow: hidden; padding-top: 5%;'})], **{})], **{})	).html