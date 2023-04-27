#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (err) console.error(err);
  else if (response.statusCode === 200) {
    const count = 0;
    const results = JSON.parse(body).results;
    const people = '/api/people/18/';
    for (let i = 0; i < results.length; i++) {
      if (results[i].characters.find(add => add.includes(people))) {
	i++;
      }
    }
    console.log(count);
  }
});
