#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, response) => {
  if (err) {
   console.error(err);
   } else {
   console.log(response);
   }
});
