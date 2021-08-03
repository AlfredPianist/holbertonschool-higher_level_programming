#!/usr/bin/node
// Script that returns a reversed list.

exports.esrever = function (list) {
  const len = list.length;
  const newList = Array.apply(undefined, Array(len));
  for (let end = len - 1, beg = 0; end >= Math.floor(len / 2); end--, beg++) {
    newList[end] = list[beg];
    newList[beg] = list[end];
  }
  return newList;
};
