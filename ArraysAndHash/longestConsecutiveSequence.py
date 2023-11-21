# https://leetcode.com/problems/longest-consecutive-sequence/
# The idea is to store the list in set to make look up faster. 
# For each number check if there is a smaller number and/or a bigger number in set.
# Time complexity: 
# n is length of nums
# O(2n) = O(n)
# Space complexity:
# O(n) for set
class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0: return 0
        numsSet = set(nums)
        start = numsSet.pop()
        end = start
        count = 1
        maxLen = 1 
        while len(numsSet) > 0:
            if start != None and start - 1 in numsSet:
                numsSet.remove(start - 1)
                start-=1
                count+=1
            else:
                start = None

            if end != None and end + 1 in numsSet:
                numsSet.remove(end + 1)
                end += 1
                count += 1
            else:
                end = None

            if start == None and end == None or len(numsSet) == 0:
                maxLen = max(count, maxLen)
                if len(numsSet) > 0:
                    start = numsSet.pop()
                    end = start
                    count = 1

        return maxLen


        