const btn = document.querySelector('#toggle_header');
const element = document.querySelector('header');

btn.addEventListener('click', () => {
	element.classList.toggle('red');
	element.classList.toggle('green');
})
