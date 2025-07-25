const { readFileSync } = require('fs');

readFileSync(process.argv[2], 'utf-8').catch(a => console.log(a));
