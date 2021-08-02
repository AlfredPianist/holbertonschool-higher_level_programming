#!/usr/bin/node
// Script that prints the second biggest number from a list of arguments
let { argv } = require('process');
argv = argv.slice(2);
const argc = argv.length;

if (argc === 0 || argc === 1) {
  console.log(0);
} else {
  const nums = [];
  for (let i = 0; i < argc; i++) {
    nums.push(parseInt(argv[i]));
  }
  nums.sort((a, b) => a - b);
  console.log(nums[argc - 2]);
}
