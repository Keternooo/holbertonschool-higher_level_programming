#!/usr/bin/node

const { writeFileSync } = require('fs');
writeFileSync(process.args[2], process.args[3]);
