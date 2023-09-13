#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (w === undefined || h === undefined) {
            const Rectangle = {};
            return 'Rectangle ${Rectangle}';
        }
        if (w <= 0 || h <= 0) {
            const Rectangle = {};
            return 'Rectangle ${Rectangle}';
        }
        this.width = w;
        this.height = h;
    }
}

module.exports = Rectangle;

