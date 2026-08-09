class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b = 0,0
        i = len(cost) - 1
        while i >= 0:
            a,b = cost[i] + min(a,b),a
            i -= 1
        return min(a,b)
        