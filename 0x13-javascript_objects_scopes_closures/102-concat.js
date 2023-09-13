#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: 102-concat.js source1 source2 final');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destination = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Can't read ${sourceFile1}: ${err.message}`);
    process.exit(1);
  }

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Can't read  ${sourceFile2}: ${err.message}`);
      process.exit(1);
    }

    const concatenatedData = data1 + data2;

    fs.writeFile(destination, concatenatedData, (err) => {
      if (err) {
        console.error(`Can't write to ${destination}: ${err.message}`);
        process.exit(1);
      }
    });
  });
});
