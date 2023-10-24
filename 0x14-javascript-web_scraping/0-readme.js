#!/usr/bin/node
'use strict';

const fs = require('fs');

if (process.argv.length !== 3) {
  console.error('Ussage: node 0-readme.js <file-path>');
  process.exit(1);
}

const fp = process.argv[2];

fs.readFile(fp, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
