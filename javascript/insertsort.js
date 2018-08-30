'use strict';

const assert = require('assert');

function insertSort(arr) {
  if (arr.length < 2) {
    return arr;
  }

  for (let i = 1; i < arr.length; i++) {
    let j = i;

    while (j >= 0 && arr[j] < arr[j - 1]) {
      const temp = arr[j];
      arr[j] = arr[j - 1];
      arr[j - 1] = temp;
      j -= 1;
    }
  }

  return arr;
}

function test() {
  assert.deepEqual(insertSort([]), []);
  assert.deepEqual(insertSort([0]), [0]);
  assert.deepEqual(insertSort([2, 1]), [1, 2]);
  assert.deepEqual(insertSort([3, 2, 1]), [1, 2, 3]);
  assert.deepEqual(
    insertSort([9, 1, 2, 6, 7, 8, 10, 11, 23, 90, 5, 9]),
    [1, 2, 5, 6, 7, 8, 9, 9, 10, 11, 23, 90]
  );
  console.log('all tests pass!');
}

test();