#!/usr/bin/node

const num = process.argv.slice(2).map(arg => parseInt(arg, 10));

if (num.length === 0) {
  console.log(0);
} else if (num.length === 1) {
  console.log(1);
} else {
  num.sort((a, b) => b - a);
  console.log(num[1]);
}
