'use strict';

const assert = require('assert');

class HashTable {
  constructor(size) {
    this.size = size;
    this.table = Array(size).fill([]);
  }

  hash(key) {
    return key % this.size;
  }

  insert(key, val) {
    const hashIdx = this.hash(key);
    const bucket = this.table[hashIdx];

    // First check if the key already exists
    const existing = bucket.find(item => item.key === key);
    if (existing) {
      existing.val = val;
      return;
    }

    // Otherwise add it
    bucket.push(new HashTableEntry(key, val));
  }

  retrieve(key) {
    const hashIdx = this.hash(key);
    const existing = this.table[hashIdx].find(item => item.key === key);
    return existing ? existing.val : null;
  }

  remove(key) {
    const hashIdx = this.hash(key);
    const bucket = this.table[hashIdx];
    const bucketIdx = bucket.findIndex(item => item.key === key);

    if (bucketIdx !== null) {
      bucket.splice(bucketIdx, 1);
    }
  }
}

class HashTableEntry {
  constructor(key, val) {
    this.key = key;
    this.val = val;
  }
}

function test() {
  const hashTable = new HashTable(5);

  assert.equal(hashTable.retrieve(1), null);

  hashTable.insert(1, 'one');
  hashTable.insert(2, 'two');
  hashTable.insert(3, 'three');

  assert.equal(hashTable.retrieve(1), 'one');

  // Verify overwriting a value works
  hashTable.insert(3, 'three!');
  assert.equal(hashTable.retrieve(3), 'three!');

  // Test retrieving key/value pair that doesn't exist
  assert.equal(hashTable.retrieve(4), null);

  hashTable.remove(1);
  assert.equal(hashTable.retrieve(1), null);

  console.log('all tests pass');
}

test();