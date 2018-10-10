'use strict';

const assert = require('assert');

class MinHeap {
  constructor(values = []) {
    this.values = values;
  }

  extractMin() {
    if (!this.values || !this.values.length) {
      return null;
    }

    if (this.values.length === 1) {
      return this.values.shift();
    }

    const min = this.values[0];
    this.values[0] = this.values.pop();
    // Rebalance when min is plucked
    this.bubbleDown(0);
    return min;
  }

  peekMin() {
    return this.values.length ? this.values[0] : null;
  }

  insert(val) {
    // Add new value as the rightmost child
    this.values.push(val);
    // Bubble the value up so that the min heap property remains intact
    this.bubbleUp(this.values.length - 1);
  }

  bubbleDown(idx) {
    // Figure out which of the node's children is smaller
    const minChildIdx = this.getSmallestChild(idx);
    if (!minChildIdx) {
      return;
    }

    // Recursively swap indices until min heap invariant is restored
    if (this.values[idx] > this.values[minChildIdx]) {
      this.swap(idx, minChildIdx);
      this.bubbleDown(minChildIdx);
    }
  }

  bubbleUp(idx) {
    if (idx === 0) {
      return;
    }

    const parentIdx = Math.floor((idx - 1) / 2);
    if (this.values[idx] < this.values[parentIdx]) {
      this.swap(idx, parentIdx);
      this.bubbleUp(parentIdx);
    }
  }

  getSmallestChild(idx) {
    const leftIdx = 2 * idx + 1;
    const rightIdx = 2 * idx + 2;
    const count = this.values.length;

    // No child nodes exist
    if (leftIdx >= count && rightIdx >= count) {
      return null;
    } else if (leftIdx >= count) {
      // Only right node exists
      return rightIdx;
    } else if (rightIdx >= count) {
      // Only left node exists
      return leftIdx;
    } else {
      // Both nodes exist so we want the one with a smaller value
      return this.values[leftIdx] < this.values[rightIdx] ? leftIdx : rightIdx;
    }
  }

  swap(a, b) {
    const temp = this.values[a];
    this.values[a] = this.values[b];
    this.values[b] = temp;
  }
}

function test() {
  let minHeap = new MinHeap();
  assert.equal(minHeap.peekMin(), null);
  assert.equal(minHeap.extractMin(), null);

  minHeap.insert(3);
  assert.equal(minHeap.peekMin(), 3);

  minHeap.insert(1);
  minHeap.insert(4);
  minHeap.insert(5);
  assert.equal(minHeap.peekMin(), 1);
  assert.equal(minHeap.extractMin(), 1);
  assert.equal(minHeap.values[0], 3);
  assert.equal(minHeap.values[1], 5);

  minHeap.insert(2);
  assert.equal(minHeap.peekMin(), 2);

  console.log("all tests pass");
}

test();