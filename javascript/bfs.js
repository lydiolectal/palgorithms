'use strict';

const assert = require('assert');
const GraphNode = require('./Graph').GraphNode;

function bfs(graph, v1, v2) {
  let queue = [v1];

  while (queue.length > 0) {
    let curr = queue.shift();
    curr.visited = true;

    if (curr.val === v2.val) {
      return curr;
    }

    let neighbors = graph[curr.val];
    neighbors.forEach(n => {
      if (!n.visited) {
        n.prev = curr;
        n.visited = true;
        queue.push(n);
      }
    });
  }
}

function test() {
  const a = new GraphNode('a');
  const b = new GraphNode('b');
  const c = new GraphNode('c');
  const d = new GraphNode('d');
  const e = new GraphNode('e');

  // Represent graph as an adjacency list
  let graph = {
    a: [b, c],
    b: [d],
    c: [d, e],
    d: [e],
    e: []
  };

  let result = bfs(graph, a, e);
  let path = [result.val];

  // // Retrace the path by following `prev` pointers
  while (result.prev) {
    path.push(result.prev.val);
    result = result.prev;
  }

  assert.deepEqual(['a', 'c', 'e'], path.reverse());
  console.log('all tests pass');
}

test();