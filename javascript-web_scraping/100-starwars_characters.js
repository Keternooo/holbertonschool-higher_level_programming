#!/usr/bin/node

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], async (a, b, c) => {
  if (a) return;
  (await JSON.parse(c)).characters.forEach(a => {
    request(a, async (d, e, f) => {
      if (d) return;
      console.log((await JSON.parse(f)).name);
    });
  });
});
