#!/usr/bin/node
// Script that prints if an argument is found
const { argv } = require('process');
const argc = argv.length - 2;

if (argc === 0) {
  console.log('No argument');
} else if (argc === 1) {
  console.log('Argument found');
} else if (argc > 1) {
  console.log('Arguments found');
}
