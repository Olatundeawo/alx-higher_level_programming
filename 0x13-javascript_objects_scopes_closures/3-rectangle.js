#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this .width = w;
    this.height = h;
  }
  if (this.width <= 0 || this.height <= 0) {
    let myObject = { }
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
