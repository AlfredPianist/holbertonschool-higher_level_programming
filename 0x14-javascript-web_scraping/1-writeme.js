#!/usr/bin/node
// Script that writes some content to a file name given as argument
const fs = require('fs');
const { argv } = require('process');

fs.writeFile(argv[2], argv[3], 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
