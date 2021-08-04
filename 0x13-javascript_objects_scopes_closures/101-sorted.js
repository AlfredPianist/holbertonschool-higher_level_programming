#!/usr/bin/node
// Script that prints a new dictionary with its values pointing to its keys.

const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}

console.log(newDict);
