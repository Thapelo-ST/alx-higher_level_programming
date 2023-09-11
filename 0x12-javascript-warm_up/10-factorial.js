#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const ans = factorial(num);
console.log(ans);
