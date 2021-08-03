#!/usr/bin/node
// Script that converts a number to another base.

exports.converter = function (base) {
  return (num) => num.toString(base);
};
