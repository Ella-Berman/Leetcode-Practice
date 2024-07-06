#You are given a string s consisting of only uppercase english 
#characters and an integer k. You can choose up to k characters 
#of the string and replace them with any other uppercase English 
#character.

#After performing at most k replacements, return the length of the 
#longest substring which contains only one distinct character.
class Solution:
    # method: sliding window
    # O(26*n)
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # count occurances of each char
        res = 0 # longest substr w k replacements so far 

        l = 0
        for r in range(len(s)):
            # increment count for current char
            count[s[r]] = 1 + count.get(s[r], 0) # if doesn't exist, 0

            # determine if valid window
            # if # of replacements needed is greater than k
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # determine max of res and current window size
            res = max(res, r-l + 1)

        return res