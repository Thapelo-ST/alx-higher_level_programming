#!/usr/bin/node

const { dict } = require('./101-data');

const IdByOccurance = {};

for (const userId in dict) {
  const occurance = dict[userId];
  // if occurance is null initialize an empty array
  if (!IdByOccurance[occurance]) {
    IdByOccurance[occurance] = [];
  }

  IdByOccurance[occurance].push(userId);
}

console.log(IdByOccurance);
