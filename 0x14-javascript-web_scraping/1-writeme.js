#!/usr/bin/node
// a script that writes a string to a file.

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8',(err,response) => {
	if (err) {
		console.error(err);
	}
	console.log('Success');
});
