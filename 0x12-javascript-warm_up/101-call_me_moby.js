#!/usr/bin/node
// Script that executes a function x times.
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
