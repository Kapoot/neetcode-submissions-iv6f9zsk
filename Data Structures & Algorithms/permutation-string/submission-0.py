class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Map = [0] * 26
        s2Map = [0] * 26

        for char in s1:
            s1Map[ord(char) - ord('a')] += 1
        
        L = 0
        R = 0
        while R < len(s2):
            s2Map[ord(s2[R]) - ord('a')] += 1
            while (R - L + 1) > len(s1):
                s2Map[ord(s2[L]) - ord('a')] -= 1
                L += 1
            if s2Map == s1Map:
                return True
            R += 1
        return False
            
 

        


        