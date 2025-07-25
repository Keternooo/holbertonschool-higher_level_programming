#!/usr/bin/node
const request = require('request');
request(process.argv[2], (e, s, b) => {
  if (e) return;
  console.log([...(b.matchAll('/people/18/'))].length);
});
