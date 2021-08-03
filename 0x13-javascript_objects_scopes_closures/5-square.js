#!/usr/bin/node
// Creation of square class inheriting from Rectangle with size.
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
