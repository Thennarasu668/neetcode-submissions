import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        count = 0
        maxHeap = []
        for g in gifts:
            heapq.heappush(maxHeap,-g)
        while count < k:
            count += 1
            gift =  heapq.heappop(maxHeap)
            rem_gift = -1 * int(abs(gift) ** 0.5)
            heapq.heappush(maxHeap,(rem_gift))
        return abs(sum(maxHeap))
        
        
        