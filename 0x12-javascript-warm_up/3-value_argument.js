#!/usr/bin/node
// Script that prints the argument value if it exist.
const { argv } = require('process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[3]);
}
