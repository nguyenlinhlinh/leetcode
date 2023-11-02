# https://leetcode.com/problems/product-of-array-except-self/description/
# Time comlexity: O(2n) = O(n)
# Space complexity: O(1) output array doesn't count as extra space
# Idea: calculate product from left to right and then calculate from right to left
class Solution:
    def productExceptSelf(self, nums):
        answer = [1 for i in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer