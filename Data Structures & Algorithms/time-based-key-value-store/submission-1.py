from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        # Dictionary to store the key-value pairs where key maps to a list of (timestamp, value) tuples
        self.data = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the (timestamp, value) tuple to the list associated with the key
        self.data[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        # If the key is not in the dictionary, return an empty string
        if key not in self.data:
            return ""
        
        # Retrieve the list of (timestamp, value) for the given key
        timestamps_values = self.data[key]
        
        # Perform binary search
        low, high = 0, len(timestamps_values) - 1
        while low <= high:
            mid = (low + high) // 2
            if timestamps_values[mid][0] <= timestamp:
                low = mid + 1
            else:
                high = mid - 1
        
        # After the loop, `high` should be pointing to the largest index 
        # where the timestamp is <= given timestamp
        if high >= 0 and timestamps_values[high][0] <= timestamp:
            return timestamps_values[high][1]
        else:
            return ""