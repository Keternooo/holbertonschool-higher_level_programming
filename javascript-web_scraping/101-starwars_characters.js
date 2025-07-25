#!/usr/bin/node

const request = require('request');
const util = require('util');
const get = util.promisify(request.get);

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], async (a, b, c) => {
  if (a) return;
  const actors = (await JSON.parse(c)).characters;
  for (let i = 0; i < actors.length; i++) {
    const req = await get({ url: actors[i], json: true });
    console.log(req.body.name);
  }
});
