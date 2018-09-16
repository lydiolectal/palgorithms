# https://leetcode.com/problems/lru-cache/description/

class Node:
    
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.key_dict = {}
        self.head = None
        self.tail = None
        
    # Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    def get(self, key):
        if key not in self.key_dict:
            return -1
        value = self.key_dict[key].value
        self.delete_by_key(key)
        new_node = self.add_to_head(key, value)
        self.key_dict[key] = new_node
        return value
           
    # Set or insert the value if the key is not already present.
    # When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
    def put(self, key, value):
        if self.capacity < 1:
            return
        # 1. Not at capacity, key isn't already in the list -> add it
        # 2. Not at capacity, key is already in the list -> pop old key off, insert at head
        #    At capacity, key is already in the list -> pop old key off, insert with new value at head
        # 3. At capacity, key isn't already in the list -> pop LRU off, insert at head
        if key in self.key_dict:
            self.delete_by_key(key)
        elif len(self.key_dict) >= self.capacity:
            key_to_delete = self.delete_from_tail()
            del self.key_dict[key_to_delete]
        
        new_node = self.add_to_head(key, value)
        self.key_dict[key] = new_node

    def add_to_head(self, key, value):
        new_node = Node(key, value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            new_node.next = old_head
            old_head.prev = new_node
            self.head = new_node
    
        return new_node 

    def delete_from_tail(self):
        key_to_delete = self.tail.key
        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
           
        return key_to_delete
    
    def delete_by_key(self, key):
        node = self.key_dict[key]
        node_prev = node.prev
        node_next = node.next
        if node == self.head and node == self.tail:
            self.head, self.tail = None, None
        elif node == self.head:
            node_next.prev = None
            self.head = node_next
        elif node == self.tail:
            node_prev.next = None
            self.tail = node_prev
        else:
            node_prev.next = node_next
            node_next.prev = node_prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)