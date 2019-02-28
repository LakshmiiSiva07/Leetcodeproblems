class Solution(object):
    def checkPossibility(self, nums):
        """
        Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
        We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        index = 0
        if(len(nums) > 2):
            for i in range(0, (len(nums) - 1)):
                if (nums[i] > nums[i + 1]):
                    count = count + 1
                    if (count == 1):
                        index = i
                    if (count > 1):
                        return False
            if (index == 0 or index == (len(nums) - 2)):
                return True
            else:
                swapped_value = nums[index]
                nums[index] = nums[index + 1] - 1
                if(nums[index] < nums[index - 1]):
                    nums[index] = swapped_value
                    nums[index + 1] = nums[index + 2] - 1
                for i in range(index-1,(len(nums) - 1)):
                    if(nums[i] > nums[i + 1]):
                        return False
        return True
