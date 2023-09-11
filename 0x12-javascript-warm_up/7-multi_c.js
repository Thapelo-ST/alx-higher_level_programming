#!/usr/bin/node

const print = 'C is fun';
let arg = parseInt(process.argv[2]);

if (!isNaN(arg)) {
  while (arg > 0) {
    console.log(print);
    arg--;
  }
} else {
  console.log('Missing number of occurances');
}
