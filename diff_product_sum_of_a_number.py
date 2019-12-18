class Solution:
"""
Given an integer number n, return the difference between the 
product of its digits and the sum of its digits.
"""
    def subtractProductAndSum(self, n: int) -> int:
        num_list = [int(x) for x in str(n)]
        prod = 1
        sumof = 0
        for num in num_list:
            prod = prod * num
            sumof = sumof + num
        return (prod - sumof)
