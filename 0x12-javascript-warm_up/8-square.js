#!/usr/bin/node
// Prints an n * n square.
const { argv } = require('process');

const term1 = parseInt(argv[2]);
const term2 = parseInt(argv[3]);

function add(a, b) {
  return a + b;
}

console.log(add(term1, term2));
