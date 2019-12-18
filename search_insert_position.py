class Solution:
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.
"""
    def searchInsert(self, nums: List[int], target: int) -> int:
            if target in nums:
                return nums.index(target)
            else:
                length = len(nums)
                value = 0
                while(target > nums[value]):
                    value = value + 1
                    if (value == length):
                        return value
                return value
