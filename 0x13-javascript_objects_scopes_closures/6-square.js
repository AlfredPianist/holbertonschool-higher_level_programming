#!/usr/bin/node
// Creation of square class inheriting from Square with method charPrint.
const Square = require('./5-square');

class Square2 extends Square {
  charPrint (c) {
    const glyph = !c ? 'X' : c;
    const iterator = Array.apply([], Array(this.height));
    iterator.forEach(() => console.log(glyph.repeat(this.width)));
  }
}
module.exports = Square2;
