#!/usr/bin/node
const { readFileSync } = require('fs');

readFileSync(process.argv[2], 'utf-8').then(a => console.log(a)).catch(a => console.log(a));
