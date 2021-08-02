#!/usr/bin/node
// Script that prints the first argument converted to integer.
const { argv } = require('process');

const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
