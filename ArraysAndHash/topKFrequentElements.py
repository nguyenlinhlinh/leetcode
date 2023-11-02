# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import Counter

class Solution:
    # Time comlexity: O(n + n + nlgn) = O(nlgn)
    # Space complexity: 2n
    # Idea: calculate frequences and then sort by frequences
    def topKFrequent(self, nums, k):
        frequences = Counter(nums)
        array =[(k,v) for k,v in frequences.items()]
        array.sort(reverse=True,key=lambda item: item[1])
        return [i[0] for i in array[:k]]
    
    # Time comlexity: O(n + n + n + n + k ) = O(n + k)
    # Space complexity: 2n = n
    # Idea: using bubble sort, 
    # 1. Count frequences 
    # 2. Put them in array where index is count and value is number
    # 3. Iterate through the array to get top K
    def topKFrequent1(self, nums, k):
        frequences = Counter(nums)
        sorted = [[] for i in range(len(nums) + 1)]
        maxCount = 0
        for number, count in frequences.items():
            sorted[count].append(number)
            if(maxCount < count):
                maxCount = count
        result = []
        for i in range(maxCount, -1, -1):
            for numbers in sorted[i]:
                result.append(numbers)
                if(len(result)) == k:
                    return result