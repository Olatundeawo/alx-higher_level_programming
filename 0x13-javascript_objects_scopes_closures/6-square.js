#!/usr/bin/node

const square = require('./5-square.js');
class Square extends square {
  charPrint(c) {
    let chars;
    if (c === undefined) {
      chars = 'X';
    } else {
      chars = c;
    }
    let i;
    let j = '';
    for (i = 0; i < this.width; i++) {
      j += chars;
    }
    for (i = 0; i < this.height; i++) {
      console.log(j);
    }
}

module.exports = Square;
