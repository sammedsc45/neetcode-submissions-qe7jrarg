class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        count = Counter(tasks)
        
        # Max heap to keep track of task frequencies, negating values to create a max-heap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Time tracker and queue to handle the cooldown
        time = 0
        q = deque()  # stores [task_count, release_time] for tasks in cooldown

        while maxHeap or q:
            time += 1  # Simulate each time unit (CPU cycle)

            # If there's a task ready to run, pop from the heap
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # Reduce task count (task completed)
                
                # If the task still has remaining instances, push it into the cooldown queue
                if cnt:
                    q.append([cnt, time + n])  # Cooldown period starts now for this task

            # Check if any task in cooldown has finished its cooldown
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])  # Reinsert into heap when cooldown ends

        return time