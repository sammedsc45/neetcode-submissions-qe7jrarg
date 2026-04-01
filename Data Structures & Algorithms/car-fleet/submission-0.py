class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        # Pair positions with speeds and sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        last_time = 0
        
        for pos, spd in cars:
            # Calculate the time needed to reach the target for the current car
            time_to_reach = (target - pos) / spd
            
            # If the time to reach is greater than last_time, it means this car forms a new fleet
            if time_to_reach > last_time:
                fleets += 1
                last_time = time_to_reach
        
        return fleets