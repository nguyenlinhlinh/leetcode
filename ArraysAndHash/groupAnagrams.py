# https://leetcode.com/problems/group-anagrams/
# The idea is storing sorted strings in a dictionary to make look up faster
# Time complexity: 
# n is length of strs
# each str has length m
# O(n * 2m) = O(n*m)

from collections import Counter
class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr in result:
                result[sortedStr].append(str)
            else:
                result[sortedStr] = [str]
        return result.values()