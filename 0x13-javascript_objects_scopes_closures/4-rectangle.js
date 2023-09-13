#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) {
      const Rectangle = {};
      return `Rectangle ${Rectangle}`;
    }
    if (w <= 0 || h <= 0) {
      const Rectangle = {};
      return `Rectangle ${Rectangle}`;
    }
    this.width = w;
    this.height = h;
  }

  // print
  print () {
    if (this.width === undefined || this.height === undefined) {
      const Rectangle = {};
      return `Rectangle ${Rectangle}`;
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  // double
  double () {
    if (this.width === undefined || this.height === undefined) {
      const Rectangle = {};
      return `Rectangle ${Rectangle}`;
    } else {
      this.width = this.width * 2;
      this.height = this.height * 2;
    }
  }

  // rotate
  rotate () {
    if (this.width === undefined || this.height === undefined) {
      const Rectangle = {};
      return `Rectangle ${Rectangle}`;
    } else {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }
}

module.exports = Rectangle;
