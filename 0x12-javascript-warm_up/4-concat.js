#!/usr/bin/node
let arg1, arg2;
if (process.argv[2] === undefined && process.argv[3] === undefined) {
  arg1 = undefined;
  arg2 = undefined;
} else {
  arg1 = process.argv[2];
  arg2 = process.argv[3];
}

console.log(arg1 + ' is ' + arg2);
