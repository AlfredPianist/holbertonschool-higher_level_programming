#!/usr/bin/node
/*
  Creation of rectangle class with width and height and methods print,
  rotate and double.
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const glyph = 'X';
    const iterator = Array.apply([], Array(this.height));
    iterator.forEach(() => console.log(glyph.repeat(this.width)));
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
