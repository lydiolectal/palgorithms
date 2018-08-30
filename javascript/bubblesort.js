'use strict';

const assert = require('assert');

function bubbleSort(arr) {
  if (arr.length < 2) {
    return arr;
  }

  let swapped = false;

  for (let i = 0; i < arr.length - 1; i++) {

    // Subtract i from n, because the final i elements are sorted
    for (let j = 0; j < arr.length - i - 1; j++) {
      // Compare current element with next and swap if out of order
      if (arr[j] > arr[j + 1]) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        swapped = true;
      }
    }

    if (!swapped) {
      break;
    }
  }

  return arr;
}

function test() {
  assert.deepEqual(bubbleSort([]), []);
  assert.deepEqual(bubbleSort([0]), [0]);
  assert.deepEqual(bubbleSort([2, 1]), [1, 2]);
  assert.deepEqual(bubbleSort([3, 2, 1]), [1, 2, 3]);
  assert.deepEqual(
    bubbleSort([9, 1, 2, 6, 7, 8, 10, 11, 23, 90, 5, 9]),
    [1, 2, 5, 6, 7, 8, 9, 9, 10, 11, 23, 90]
  );
  console.log('all tests pass!');
}

test();