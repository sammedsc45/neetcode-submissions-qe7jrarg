from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize the LRU cache with the given capacity
        self.capacity = capacity
        self.cache = OrderedDict()  # Using OrderedDict to maintain the order of keys

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Key not found
        else:
            # Move the accessed key to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the key to the end to mark it as recently used
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used key-value pair from the cache
            self.cache.popitem(last=False)
        
        # Add the new key-value pair to the cache
        self.cache[key] = value