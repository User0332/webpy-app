const player = document.getElementById("player")

window.addEventListener("keydown", (e) => {
	e.preventDefault()

	const key = e.key

	switch (key) {
		case "ArrowUp":
			player.y+=1
			break

		case "ArrowDown":
			break

		case "ArrowLeft":
			break

		case "ArrowRight":
			break

		default: break
	}
})