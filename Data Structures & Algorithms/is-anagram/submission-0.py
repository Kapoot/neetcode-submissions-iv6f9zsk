class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap1 = {}
        hashmap2 = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in hashmap1:
                hashmap1[s[i]] = 0
            else:
                hashmap1[s[i]] += 1
            
            if t[i] not in hashmap2:
                hashmap2[t[i]] = 0
            else:
                hashmap2[t[i]] += 1 
        

        return hashmap1.items() == hashmap2.items()
        



        