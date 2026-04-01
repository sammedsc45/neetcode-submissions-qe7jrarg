class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # Stack to store indices of the temperatures array

        for i in range(n):
            # While stack is not empty and current temperature is greater than the temperature at index stored in stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            stack.append(i)
        
        return res