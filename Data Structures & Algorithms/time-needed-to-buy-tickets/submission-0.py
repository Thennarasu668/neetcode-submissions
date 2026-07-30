from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        for i,t in enumerate(tickets):
            q.append((t,i))
        time = 0
        while q:
            ticket,index = q.popleft()
            time += 1
            if (ticket - 1) == 0:
                if index == k:
                    return time
            else:
                q.append((ticket - 1,index))

        