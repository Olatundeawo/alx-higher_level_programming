#!/usr/bin/node
// A script that reads and prints the cotent of a file

const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, response) => {
	if (err) {
		console.error(err);
	}
	console.log(response);
});
