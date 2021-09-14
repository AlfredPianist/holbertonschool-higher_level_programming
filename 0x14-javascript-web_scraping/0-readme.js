#!/usr/bin/node
// Script that prints the contents from a file given as argument
const fs = require('fs');
const { argv } = require('process');

fs.readFile(argv[2], (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString('utf-8'));
  }
});
