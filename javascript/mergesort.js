const assert = require('assert');

function mergeSort(list) {
  if (list.length <= 1) return list;

  const mid = Math.floor(list.length / 2);
  const left = list.slice(0, mid);
  const right = list.slice(mid, list.length);

  return merge(left, right);
}

function merge(left, right) {
  const l = mergeSort(left);
  const r = mergeSort(right);
  let lPtr = l && l.length > 0 ? 0 : null;
  let rPtr = r && r.length > 0 ? 0 : null;

  let result = [];

  while ((lPtr !== null && l.length > 0 && lPtr < l.length)
    || (rPtr !== null && r.length > 0 && rPtr < r.length)) {

    const lVal = l[lPtr] || null;
    const rVal = r[rPtr] || null;

    if (lVal === null || lVal === undefined || (rVal && rVal < lVal)) {
      result.push(rVal);
      rPtr += 1;
    } else if (rVal === null || rVal === undefined || (lVal && lVal <= rVal)) {
      result.push(lVal);
      lPtr += 1;
    }
  }

  return result;
}

function test() {
  assert.deepEqual(mergeSort([]), []);
  assert.deepEqual(mergeSort([0]), [0]);
  assert.deepEqual(mergeSort([2, 1]), [1, 2]);
  assert.deepEqual(mergeSort([3, 2, 1]), [1, 2, 3]);
  assert.deepEqual(
    mergeSort([9, 1, 2, 6, 7, 8, 10, 11, 23, 90, 5, 9]),
    [1, 2, 5, 6, 7, 8, 9, 9, 10, 11, 23, 90]
  );
  console.log('all tests pass!');
}

test();