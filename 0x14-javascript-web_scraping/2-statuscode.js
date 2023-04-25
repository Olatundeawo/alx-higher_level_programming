#!/usr/bin/node
// a script that display the status code of a GET request.

const request = require('request');
request(process.argv[2], (err, response) => {
	if (err) {
		console.error(err);
	}
	console.log('code:', response.statusCode);
});
