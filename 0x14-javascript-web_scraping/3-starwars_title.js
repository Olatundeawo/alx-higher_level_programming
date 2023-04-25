#!/usr/bin/node
const request = require('request');
requestUrl = 'https://swapi-api.alx-tools.com/api/films/';
request(requestUrl + process.argv[2], (err, response, body) => {
  if (err) console.error(err);
  else console.log(JSON.parse(body).title);
});
