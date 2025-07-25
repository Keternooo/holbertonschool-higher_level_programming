#!/usr/bin/node

const { readFileSync } = require('fs');
const file = readFileSync(process.argv[2], 'utf-8');
console.log(file);
