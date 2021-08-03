#!/usr/bin/node
// Script that returns the number of occurrences in a list:

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach((val) => (
    counter = searchElement === val ? counter + 1 : counter + 0));
  return counter;
};
