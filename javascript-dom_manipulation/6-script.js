document.addEventListener('DOMContentLoaded', async () => {
	const req = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
	const res = await req.json();
	document.getElementById('character').textContent = res['name'];
})
