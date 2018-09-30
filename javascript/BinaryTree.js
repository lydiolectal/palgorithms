'use strict';

const assert = require('assert');

class TreeNode {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function insert(tree, newVal) {
  const newNode = new TreeNode(newVal);
  if (newVal < tree.val) {
    if (tree.left) {
      insert(tree.left, newVal);
    } else {
      tree.left = newNode;
    }
  } else {
    if (tree.right) {
      insert(tree.right, newVal);
    } else {
      tree.right = newNode;
    }
  }
}

function lookup(tree, val) {
  if (tree.val === val) {
    return true;
  }

  if (val < tree.val) {
    if (tree.left) {
      return lookup(tree.left, val);
    } else {
      return false;
    }
  } else {
    if (tree.right) {
      return lookup(tree.right, val);
    } else {
      return false;
    }
  }
}

function test() {
  let baseTree = new TreeNode(3);
  baseTree.left = new TreeNode(2);
  baseTree.right = new TreeNode(4);

  insert(baseTree, 1);
  assert.equal(baseTree.left.left.val, 1);

  insert(baseTree, 5);
  assert.equal(baseTree.right.right.val, 5);

  assert.equal(lookup(baseTree, 4), true);
  assert.equal(lookup(baseTree, 6), false);

  console.log('all tests pass');
}

test();

