#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let q = 0; q < x; q++) {
    theFunction();
  }
};
