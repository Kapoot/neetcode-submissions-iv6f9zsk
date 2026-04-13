class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        my_map = collections.defaultdict(list)
        
        for word in strs:
            res = [0] * 26
            for s in word:
                res[ord('z') - ord(s)] += 1
            my_map[tuple(res)].append(word)
        
        return my_map.values()
            
            



        


        