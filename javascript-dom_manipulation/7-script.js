document.addEventListener('DOMContentLoaded', async () => {
	const req = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
	const res = await req.json();

	res['results'].forEach(a => {
		document.querySelector('#list_movies').innerHTML += '<li>' + a['title'] + '</li';
	})
})
