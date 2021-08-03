#!/usr/bin/node
// Creation of rectangle class with width and height and a print method.

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
}
module.exports = Rectangle;
