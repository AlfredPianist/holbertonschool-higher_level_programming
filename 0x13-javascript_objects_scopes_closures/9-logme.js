#!/usr/bin/node
// Script that prints the arguments printed and the new value.

exports.logMe = (function (item) {
  let count = 0;
  function print (item) {
    console.log(`${count}: ${item}`);
    count++;
  }
  return print;
}());
