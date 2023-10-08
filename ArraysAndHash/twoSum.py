# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        numToIndex = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numToIndex:
                return [i, numToIndex[comp]]
            numToIndex[nums[i]] = i
# test cases
one = [[2,7,11,15], 9]
two = [[3,2,4], 6]
three = [[3,3], 6]

s = Solution()
s.twoSum(one[0], one[1])