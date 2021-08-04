#!/usr/bin/node
// Script that concatenates two files into a new one.
let { argv } = require('process');
const fs = require('fs');

argv = argv.slice(2);
const argc = argv.length;

if (argc === 3) {
  const fileA = fs.readFileSync(argv[0]);
  const fileB = fs.readFileSync(argv[1]);
  fs.writeFileSync(argv[2], fileA + fileB);
}
