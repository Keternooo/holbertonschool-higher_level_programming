const btn = document.querySelector('#add_item');
const element = document.querySelector('ul');

btn.addEventListener('click', () => {
	element.innerHTML += '<li>Item</li>'
})
