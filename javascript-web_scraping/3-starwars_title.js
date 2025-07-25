#!/usr/bin/node

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], async (err, st, bo) => {
  if (err) return;
  console.log((await JSON.parse(bo)).title);
});
