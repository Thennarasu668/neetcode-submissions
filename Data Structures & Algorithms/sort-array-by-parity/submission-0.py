class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res1 = []
        res2 = []
        for n in nums:
            if n % 2 == 0:
                res1.append(n)
            else:
                res2.append(n)
        return res1 + res2

        