import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)  #count of items
        
        max_heap  = [-cnt for cnt in count.values()]

        heapq.heapify(max_heap)

        print(max_heap)

        time = 0

        cooldown = deque()

        while max_heap or cooldown:

            time +=1

            if max_heap:
                c = heapq.heappop(max_heap)

                c +=1

                if c < 0:
                    cooldown.append((c, time+n))

            if cooldown and cooldown[0][1] == time:
                task_ready = cooldown.popleft()[0]  # Remove from cooldown
                heapq.heappush(max_heap, task_ready)
        return time


        