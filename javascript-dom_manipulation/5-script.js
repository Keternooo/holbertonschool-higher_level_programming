const btn = document.getElementById('update_header');

btn.addEventListener('click', () => {
	document.querySelector('header').textContent = 'New Header!!!';
})

