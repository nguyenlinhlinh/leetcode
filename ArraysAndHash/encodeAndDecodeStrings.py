# Encode using length of string and # 
# Remember to add offset when slicing (i + length + 1)
# https://neetcode.io/problems/string-encode-and-decode
class Solution:

    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s):
        result = []
        start = 0
        i = 0
        while i < len(s):
            if s[i] == '#':
                length = int(s[start:i])
                end = i + length + 1
                result.append(s[i + 1: end])
                start = end
                i = end
                continue
            i+=1
        return result