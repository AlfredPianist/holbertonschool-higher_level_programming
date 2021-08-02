#!/usr/bin/node
// Prints an n * n square.
const { argv } = require('process');

const side = parseInt(argv[2]);
if (isNaN(side)) {
  console.log('Missing size');
} else if (side > 0) {
  const row = 'X';
  const iterator = Array.apply([], Array(side));
  iterator.forEach(() => console.log(row.repeat(side)));
}
