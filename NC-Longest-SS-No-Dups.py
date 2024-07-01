# Given a string s, find the length of the longest substring 
# without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charSet = set()
        l = 0

        for r in range(len(s)):
            # remove all duplicates
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res