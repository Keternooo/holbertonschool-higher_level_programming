#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  console.log(response && response.statusCode); // Print the response status code if a response was received
});
