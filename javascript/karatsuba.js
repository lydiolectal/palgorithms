'use strict';

const assert = require('assert');

function karatsuba(x, y) {
  const b = 10;

  if (x < b || y < b) {
    return x * y;
  }

  const m = Math.max(x.toString().length, y.toString().length);
  const m2 = Math.floor(m / 2);

  const xHigh = Math.floor(x / Math.pow(b, m2));
  const xLow = x % Math.pow(b, m2);

  const yHigh = Math.floor(y / Math.pow(b, m2));
  const yLow = y % Math.pow(b, m2);

  const z0 = karatsuba(xLow, yLow);
  const z1 = karatsuba((xLow + xHigh), (yLow + yHigh));
  const z2 = karatsuba(xHigh, yHigh);

  return (z2 * Math.pow(b, 2 * m2)) + ((z1 - z2 - z0) * Math.pow(b, m2)) + z0;
}

function test() {
  assert.equal(karatsuba(2, 8), 16);
  assert.equal(karatsuba(10, 10), 100);
  assert.equal(karatsuba(10, 11), 110);
  assert.equal(karatsuba(219, 135), 29565);
  assert.equal(karatsuba(12345, 54321), 670592745);
  console.log('tests pass');
}

test();