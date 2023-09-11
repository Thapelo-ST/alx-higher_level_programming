#!/usr/bin/node

const print = 'X';
let arg = parseInt(process.argv[2]);
let i = 0; const t = arg;

if (!isNaN(arg)) {
  while (arg > 0) {
    let row = '';
    for (i = 0; i < t; i++) {
      row += print;
    }
    console.log(row);
    arg--;
  }
} else {
  console.log('Missing size');
}
