document
	.querySelectorAll("input[required]")
	.forEach((element) => {
		element.oninput = 
			() => element.setCustomValidity("")

		element.oninvalid = 
			() => element.setCustomValidity(
				`Please enter a ${element.getAttribute("name")}`
			)
	})

document.getElementById("login-sumbit")
	.onclick = (e) => {
		e.preventDefault()

		const [username, password] =
			document.getElementsByTagName("input")

		if (!(username.reportValidity() || password.reportValidity()))
			return

		fetch("/login", {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				username: username.value,
				password: password.value
			})
		}).then(() => window.location = "/dashboard")
	}