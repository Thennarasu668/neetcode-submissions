class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for index,val in enumerate(nums):
            my_dict[val]=index
        for i in range(len(nums)):
            des=target-nums[i]
            if des in my_dict :
                if i>my_dict[des] and my_dict[des]!=i:
                    return [my_dict[des],i]
                if my_dict[des]!=i:
                    return [i,my_dict[des]]