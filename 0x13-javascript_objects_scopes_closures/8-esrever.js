#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((item, idx) => list[list.length - 1 - idx]);
};
