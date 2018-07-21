const assert = require('assert');

let i = 0;
function quickSort(list) {
  if (list.length <= 1) return list;

  // Define a pivot
  const pivot = list[list.length - 1];
  let left = [];
  let right = [pivot];

  list.forEach((item, idx) => {
    if (idx === list.length - 1) return;

    // If the number in the list is less than pivot, add it to left
    if (item <= pivot) {
      left.push(item);
      // Else if it's greater than pivot, add it to right
    } else {
      right.push(item);
    }
  });

  // Repeat for each half
  left = quickSort(left);
  right = quickSort(right);

  return left.concat(right);
}

function test() {
  assert.deepEqual(quickSort([]), []);
  assert.deepEqual(quickSort([0]), [0]);
  assert.deepEqual(quickSort([2, 1]), [1, 2]);
  assert.deepEqual(quickSort([3, 2, 1]), [1, 2, 3]);
  assert.deepEqual(
    quickSort([9, 1, 2, 6, 7, 8, 10, 11, 23, 90, 5, 9]),
    [1, 2, 5, 6, 7, 8, 9, 9, 10, 11, 23, 90]
  );
  console.log('all tests pass!');
}

test();