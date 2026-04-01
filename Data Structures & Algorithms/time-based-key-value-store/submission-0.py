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
        
        # Retrieve the list of (timestamp, value) tuples for the given key
        timestamps_values = self.data[key]
        
        # Use binary search to find the largest timestamp <= given timestamp
        i = bisect_right(timestamps_values, (timestamp, chr(255))) - 1
        
        # If the index is valid, return the corresponding value; otherwise, return an empty string
        if i >= 0:
            return timestamps_values[i][1]
        else:
            return ""