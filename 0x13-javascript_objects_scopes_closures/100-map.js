#!/usr/bin/node
/*
  Script that prints a new list with each value from another list multiplied by
  its index.
*/
const list = require('./100-data').list;
const newList = list.map((val, idx) => val * idx);

console.log(list);
console.log(newList);
