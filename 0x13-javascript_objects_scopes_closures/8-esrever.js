#!/usr/bin/node

exports.esrever = function (list) {
  const newArray = [];
  let i;
  let lastElement = list.length - 1;
  for (i=lastElement; i >= 0; i--) {
    newArray.push(list[i]);
  }
  return newArray;
};
