#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this .width = w;
      this.height = h;
    }
  }
  
  print () {
    let i;
    let j = '';
    for (i = 0; i < this.width; i++) {
      j += 'X';
    }
    for (i = 0; i <  this.height; i++) {
      console.log(j);
    }
  }
}

module.exports = Rectangle;
