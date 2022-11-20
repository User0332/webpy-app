const input = document.getElementById("calc-input")
const submit = document.getElementById("submit")
const del = document.getElementById("del")
const clear = document.getElementById("clear")

window.addEventListener("keydown", (e) => {
	e.preventDefault()

	const key = e.key

	if (key == "Enter" || key == "=") {
		submit.click() 
		return
	}

	if (key == "Backspace") {
		del.click()
		return
	}

	if (key == 'c') {
		clear.click()
		return
	}

	if ("12345667890+-/*".includes(key))
		input.textContent+=key
})

document.querySelectorAll(".calculator-button")
	.forEach((button) => {
		if (button.id === "del") {
			button.onclick = () => 
				input.textContent = 
					input.textContent.substring(0, input.textContent.length-1)	
			return
		}

		if (button.id === "clear") {
			button.onclick = () => input.textContent = ""
			return
		}

		button.onclick = () => input.textContent+=button.textContent
	})

submit.onclick = () => {
	try { input.textContent = eval(input.textContent) }
	catch (e) { alert("Invalid Expression!") }
}

	