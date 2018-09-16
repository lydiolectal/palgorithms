'use strict';

function Node(key, value, prev = null, next = null) {
  this.key = key;
  this.value = value;
  this.prev = prev;
  this.next = next;
}

/**
* @param {number} capacity
*/
var LRUCache = function (capacity) {
  this.capacity = capacity;

  // Hashtable for tracking which items are currently in the cache
  this.keys = {};

  // Pointers for linked list (head = most recently accessed)
  this.head = null;
  this.tail = null;
};

/** 
 * Return the key's value or -1 if it doesn't exist in the cache
* @param {number} key
* @return {number}
*/
LRUCache.prototype.get = function (key) {
  console.log('get', key);
  if (!(key in this.keys)) {
    return -1;
  }

  // Get the node associated with the key in order to get its value
  const { value } = this.keys[key];
  // Remove the node from its current position and promote it to the head of the list
  this.remove(this.keys[key]);
  const newHead = this.push(key, value);
  this.keys[key] = newHead;

  return value;
};

/** 
* @param {number} key 
* @param {number} value
* @return {void}
*/
LRUCache.prototype.put = function (key, value) {
  console.log('put', key, value);
  if (this.capacity < 1) {
    return;
  }

  // If the item is already in the cache, remove the old version of it
  if (key in this.keys) {
    const targetNode = this.keys[key];
    this.remove(targetNode);
  } else if (Object.keys(this.keys).length > this.capacity) {
    // If the item is not in the cache but we're at capacity, remove the LRU item
    const nodeToDelete = this.pop();
    delete this.keys[nodeToDelete.key];
  }

  // Otherwise just add the node to the head and update hashtable
  const newHead = this.push(key, value);
  this.keys[key] = newHead;
};

/**
 * Add a new node to the head of the cache's linked list
 * @param {number} key 
 * @param {number} value 
 * @return {Node}
 */
LRUCache.prototype.push = function (key, value) {
  const newHead = new Node(
    key,
    value,
    null,
    this.head
  );

  if (!this.head) {
    this.tail = newHead;
  } else {
    const oldHead = this.head;
    newHead.next = oldHead;
    oldHead.prev = newHead;
  }

  this.head = newHead;
  return newHead;
}

/**
 * Remove the node at the tail of the cache's linked list and return its 'key' value
 * @return {Node} 
 */
LRUCache.prototype.pop = function () {
  const oldTail = this.tail;

  if (this.head.key === this.tail.key) {
    this.head = null;
    this.tail = null;
  } else {
    this.tail = this.tail.prev;;
    this.tail.next = null;
  }

  return oldTail;
}

/**
 * 
 * @param {Node} node 
 */
LRUCache.prototype.remove = function (node) {
  const { prev, next } = node;
  console.log('remove', node, prev, next);

  if (node.key === this.head.key && node.key === this.tail.key) {
    // If there's only one item in the list, reset head and tail
    this.head = null;
    this.tail = null;
  } else if (node.key === this.head.key) {
    this.head = next;
    this.head.prev = null;
  } else if (node.key === this.tail.key) {
    this.tail = prev;
    this.tail.next = null;
  } else {
    node.prev.next = next;
    node.next.prev = prev;
  }
}

/** 
* Your LRUCache object will be instantiated and called as such:
* var obj = Object.create(LRUCache).createNew(capacity)
* var param_1 = obj.get(key)
* obj.put(key,value)

const cache = new LRUCache(2);

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
*/