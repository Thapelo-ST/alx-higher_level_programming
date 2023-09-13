#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (num) {
    if (num === 0) {
      return '';
    } else {
      const remainder = num % base;
      const quotient = Math.floor(num / base);
      let remainderString = remainder.toString();

      // Map values greater than 9 to hexadecimal characters
      if (base === 16 && remainder > 9) {
        remainderString = String.fromCharCode(87 + remainder);
      }

      return convertToBase(quotient) + remainderString;
    }
  };
};
