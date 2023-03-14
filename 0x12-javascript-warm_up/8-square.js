#!/usr/bin/node

const x = process.argv[2];

if (isNaN(Number(x))) {
  console.log('Missing size');
} else {
  let i, j;
  for (i = 0; i < x; i++) {
      for (j = 0; j < x; j++) {
	  console.log('X');
      }
      console.log('');
  }
}
