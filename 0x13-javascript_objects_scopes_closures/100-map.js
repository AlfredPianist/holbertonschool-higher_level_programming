#!/usr/bin/node
// Script that converts a number to another base.

const list = require('./100-data').list;
const newList = list.map((val, idx) => val * idx);

console.log(list);
console.log(newList);
