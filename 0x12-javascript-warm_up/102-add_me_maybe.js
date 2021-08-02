#!/usr/bin/node
// Script that adds 1 and executes a function.
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
