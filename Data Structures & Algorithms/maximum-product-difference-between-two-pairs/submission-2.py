class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_first = float('-inf')
        max_second = float('-inf')
        min_first = float('inf')
        min_second = float('inf')
        for n in nums:
            if n > max_first:
                max_second = max_first
                max_first = n
            elif n > max_second:
                max_second = n
            if n < min_first:
                min_second = min_first
                min_first = n
            elif n < min_second:
                min_second = n

        return (max_first * max_second) -  (min_first * min_second)        