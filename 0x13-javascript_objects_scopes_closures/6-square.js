#!/usr/bin/node
/*
  Creation of square class inheriting from Rectangle with size and
  method charPrint.
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const glyph = c === undefined ? 'X' : c;
    const iterator = Array.apply([], Array(this.height));
    iterator.forEach(() => console.log(glyph.repeat(this.width)));
  }
}
module.exports = Square;
