const gameTitle = document.getElementById("gametitle")
const username = gameTitle.attributes.getNamedItem("name").value
gameTitle.textContent = `${username}'s Game!`

const playerPos = {
	x: 0,
	y: 0
}

const gameboard = [
	[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

window.addEventListener("keydown", (e) => {
	e.preventDefault()

	const key = e.key

	switch (key) {
		case "ArrowUp":
			playerPos.y+=1
			break

		case "ArrowDown":
			playerPos.y-=1
			break

		case "ArrowLeft":
			playerPos.x-=1
			break

		case "ArrowRight":
			playerPos.x+=1
			break

		default: break
	}
})