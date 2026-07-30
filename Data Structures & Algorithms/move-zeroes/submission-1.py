class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                if j <= i:
                    j = i + 1
                while j < (len(nums) - 1) and nums[j] == 0:
                    j += 1
                if j < len(nums):
                    nums[i],nums[j] = nums[j],nums[i]
            i += 1
