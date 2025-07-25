#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/', (e, s, b) => {
	if(e) return;
	console.log([...(b.matchAll('https://swapi-api.hbtn.io/api/people/18/'))].length);
});
