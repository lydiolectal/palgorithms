'use strict';

class GraphNode {
  constructor(val) {
    this.prev = null;
    this.val = val;
    this.visited = false;
  }
}

module.exports = {
  GraphNode
};