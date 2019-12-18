class Solution:
"""
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
"""
    def isHappy(self, n: int) -> bool:
        sum = n
        sum_list = []
        while(sum != 1):
           num_list = [int(x) for x in str(sum)]
           sum = 0
           for num in num_list:
               sum = sum + (num * num)
           if sum in sum_list:
               return False
           sum_list.append(sum)
        return True
