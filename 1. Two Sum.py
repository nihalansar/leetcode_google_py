'''
Problem URL : https://leetcode.com/problems/two-sum/
Difficulty Level : Easy
Solution :  We are using hash table or dictionary to solve the problem
'''

class Solution(object):
    def twoSum(self, nums, target):
        m = {}
        for index_i, i in enumerate(nums):
            j = target - i
            if j in m:
                return [m[j], index_i]
            m[i] = index_i