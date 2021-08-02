#!/usr/bin/node
// Script that prints the argument value if it exist.
const { argv } = require('process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  argv.slice(2).forEach((val) => {
    console.log(val);
  });
}
