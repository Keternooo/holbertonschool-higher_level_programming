#!/usr/node/bin

const request = require('request');
request(process.argv[2], async (e, s, b) => {
  if (e) return;
  const obj = {};
  (await JSON.parse(b)).forEach((a, i) => {if (a.completed) obj[i + 1] = a.userId; });
  console.log(obj);
});
