#!/usr/bin/node

const request = require('request');
request(process.argv[2], async (e, s, b) => {
  if (e) return;
  const obj = {};
  (await JSON.parse(b)).forEach((a, i) => {
    if (a.completed) obj[a.userId] === undefined ? obj[a.userId] = 1 : obj[a.userId] += 1;
  });
  console.log(obj);
});
