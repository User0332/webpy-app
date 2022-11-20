document
	.querySelectorAll("img.icon-button")
	.forEach((button) => 
		button.onclick = 
			() => window.location.href = `/${button.id}`
	)