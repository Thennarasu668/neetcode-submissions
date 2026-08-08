class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_map = {}
        for i in range(len(nums2)):
            for j in range(i + 1,len(nums2)):
                if nums2[i] < nums2[j]:
                    next_map[nums2[i]] = nums2[j]
                    break
        res = []
        for n in nums1:
            if n in next_map:
                res.append(next_map[n])
            else:
                res.append(-1)
        return res

        