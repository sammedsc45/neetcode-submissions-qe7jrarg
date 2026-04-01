class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If the total gas is less than total cost, we can't complete the circuit
        if sum(gas) < sum(cost):
            return -1
        
        total = 0  # Running total of gas in the tank
        start = 0  # Start station index
        
        # Traverse each station
        for i in range(len(gas)):
            total += (gas[i] - cost[i])  # Update total gas after visiting station i
            
            # If at any point the total becomes negative, reset start point
            if total < 0:
                total = 0  # Reset total gas
                start = i + 1  # Start from the next station
                
        return start  # Return the starting station index