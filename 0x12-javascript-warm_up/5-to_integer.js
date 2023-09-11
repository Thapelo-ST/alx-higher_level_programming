#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (parseInt(process.argv[2])) {
  console.log('My number: ' + `${parseInt(process.argv[2])}`);
} else if (isNaN(parseInt(process.argv[2])) === true) {
  console.log('Not a number');
}
