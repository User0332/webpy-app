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
		<pyx>
			<html>
				<head>
					<script src="../static/js/game.js" defer></script>
					<link rel="stylesheet" href="../static/css/theme.css"></link>
					<link rel="stylesheet" href="../static/css/game.css"></link>
					<title>Game</title>
				</head>
				<body class="page-center" style="overflow: hidden; padding-top: 5%;">
					<h1 id="gametitle" name={username}></h1>
						<canvas id="gamearea">
							<img id="player" src="../static/images/player.png"></img>
						</canvas>
				</body>
			</html>
		</pyx>
	).html