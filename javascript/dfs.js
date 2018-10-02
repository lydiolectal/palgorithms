'use strict';

const GraphNode = require('./Graph').GraphNode;

function dfs(graph, v1, v2) {
  let stack = [v1];

  while (stack.length > 0) {
    const curr = stack.pop();

    if (curr.val === v2.val) {
      curr.visited = true;
      return curr;
    }

    if (!(curr.visited)) {
      curr.visited = true;
      stack.push(...graph[curr.val]);
    }
  }
}

function dfsRecursive(graph, v1, v2) {
  v1.visited = true;

  if (v1.val === v2.val) {
    return v2;
  }

  const neighbors = graph[v1.val];
  for (let i = 0; i < neighbors.length; i++) {
    const n = neighbors[i];
    if (!n.visited) {
      let found = dfsRecursive(graph, n, v2);
      if (found) {
        return found;
      }
    }
  }

  return null;
}

function test() {
  const a = new GraphNode('a');
  const b = new GraphNode('b');
  const c = new GraphNode('c');
  const d = new GraphNode('d');
  const e = new GraphNode('e');
  const f = new GraphNode('f');
  let nodes = [a, b, c, d, e, f];

  // Represent graph as an adjacency list
  const graph = {
    a: [b, c],
    b: [d],
    c: [d, e, f],
    d: [e],
    e: [],
    f: []
  };

  const result = dfs(graph, a, f);
  console.log('result: ', result);

  // Reset
  nodes = nodes.map(n => n.visited = false);

  const resultRecursive = dfsRecursive(graph, a, f);
  console.log('recursive: ', resultRecursive);
}

test();