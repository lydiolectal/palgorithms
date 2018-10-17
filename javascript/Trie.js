const assert = require('assert');

class TrieNode {
  constructor(val, isEndOfWord = false, children = {}) {
    this.val = val;
    this.isEndOfWord = isEndOfWord;

    // Map of keys to TrieNodes
    this.children = children;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode(null);
  }

  /**
   * Inserts a word into the trie. 
   * @param {string} word
   * @return {void}
   */
  insert(word) {
    const len = word.length;
    let currNode = this.root;

    // For each character in word, see if it already has a path
    for (let i = 0; i < len; i++) {
      const currChar = word[i];
      const isEndOfWord = i === len - 1;

      // If the prefix doesn't exist, add it
      if (!(currChar in currNode.children)) {
        const newNode = new TrieNode(currChar, isEndOfWord);
        currNode.children[currChar] = newNode;
      } else if (isEndOfWord) {
        currNode.children[currChar].isEndOfWord = true;
      }

      currNode = currNode.children[currChar];
    }
  }

  /**
   * Returns if the word is in the trie. 
   * @param {string} word
   * @return {boolean}
   */
  search(word) {
    let currNode = this.root;

    for (let i = 0; i < word.length; i++) {
      const currChar = word[i];

      if (currChar in currNode.children) {
        currNode = currNode.children[currChar];
      } else {
        return false;
      }
    }

    return currNode.isEndOfWord;
  }

  /**
   * Returns if there is any word in the trie that starts with the given prefix. 
   * @param {string} prefix
   * @return {boolean}
   */
  startsWith(prefix) {
    let currNode = this.root;

    for (let i = 0; i < prefix.length; i++) {
      const currChar = prefix[i];

      if (currChar in currNode.children) {
        currNode = currNode.children[currChar];
      } else {
        return false;
      }
    }

    return true;
  }
}

function test() {
  const trie = new Trie();
  trie.insert('abc');
  trie.insert('ade');
  trie.insert('def');
  // console.log(JSON.stringify(trie));

  assert.equal(trie.search('abc'), true);
  assert.equal(trie.search('abcd'), false);

  assert.equal(trie.startsWith('ab'), true);
  assert.equal(trie.startsWith('g'), false);
  console.log('all tests pass');
}

test();