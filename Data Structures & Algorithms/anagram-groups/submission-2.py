class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = collections.defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char) - ord('a')] += 1
            hashmap[tuple(arr)].append(word)
        return list(hashmap.values())