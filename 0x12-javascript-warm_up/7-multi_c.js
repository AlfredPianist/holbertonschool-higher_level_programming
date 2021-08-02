#!/usr/bin/node
// Prints n times the message "C is fun".
const { argv } = require('process');

const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  const iterator = Array.apply([], Array(num));
  iterator.forEach(() => console.log('C is fun'));
}
