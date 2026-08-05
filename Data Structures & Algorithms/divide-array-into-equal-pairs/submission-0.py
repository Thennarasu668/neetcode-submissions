class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n,0) + 1
        val = len(nums) // 2
        for k,v in freq_map.items():
            if v % 2:
                return False
        return True
    
