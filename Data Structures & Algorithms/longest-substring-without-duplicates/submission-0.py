class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0 

        count = 0
        duplicate = set()
        L = 0
        R = 0
        max_count = 0

        while R < len(s):
            while s[R] in duplicate:
                duplicate.remove(s[L])
                L += 1
                count -= 1
                
            duplicate.add(s[R])
            count += 1
            max_count = max(max_count, count)
            R += 1
        return max_count
            
        
        