#!/usr/bin/node

const request = require('request');
const { writeFileSync } = require('fs');
request(process.argv[2], (e, s, b) => {
  if (e) return;
  writeFileSync(process.argv[3], b);
});
