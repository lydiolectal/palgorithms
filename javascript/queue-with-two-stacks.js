'use strict';

class QueueWithTwoStacks {
  constructor() {
    this.in = [];
    this.out = [];
  }

  enqueue(elem) {
    // Elements are always added to the `in` stack,
    // which means the first element is always at the head of the array
    this.in.push(elem);
  }

  dequeue() {
    // If there are elements in the `out` stack, they are guaranteed to be in reverse order
    // from when they were added (because elements are enqueued via the `in` stack)
    if (this.out.length > 0) {
      // As long as `out` is not empty, we can pop the last element, which for the sake of the problem is O(1)
      return this.out.pop();
    }

    if (this.in.length > 0) {
      while (this.in.length > 0) {
        // Push everything from `in` into `out` in reverse order, ensuring earliest element is on top
        const top = this.in.pop();
        this.out.push(top);
      }

      return this.out.pop();
    }

    return null;
  }
}