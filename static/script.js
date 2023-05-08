function fill() {
	fetch("/fill", {method: "POST",
		body: JSON.stringify({
			amount: 888
		})
	});
}

async function send() {
	const resultDiv = document.getElementById('result');
	const waitP = document.createElement('p');
	waitP.textContent = 'Очікуйте, повідомлення відправляються...';
	waitP.style.color = 'orange';
	waitP.style.fontSize = '30px';
	waitP.style.fontFamily = 'Arial, sans-serif';
	resultDiv.appendChild(waitP);
	const response = await fetch("/send", {method: "POST"});
	const data = await response.json();
	resultDiv.removeChild(resultDiv.lastElementChild);
	const doneP = document.createElement('p');
	const failedP = document.createElement('p');
	doneP.textContent = `Успішно надісланих повідомлень: ${data.done}`;
	doneP.style.color = 'green';
	doneP.style.fontSize = '30px';
	doneP.style.fontFamily = 'Arial, sans-serif';
	failedP.textContent =  `Не надіслано повідомлень: ${data.failed.length}`;
	failedP.style.color = 'red';
	failedP.style.fontSize = '30px';
	failedP.style.fontFamily = 'Arial, sans-serif';
	resultDiv.appendChild(doneP);
	resultDiv.appendChild(failedP);
}

document.getElementById("fill").addEventListener("click", fill);
document.getElementById("send").addEventListener("click", send);
