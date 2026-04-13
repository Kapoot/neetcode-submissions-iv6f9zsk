class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, num in enumerate(nums):
            
            complement = target - num

            if complement in hashmap:
                return [i,hashmap.get(complement)] if hashmap.get(complement) > i else [hashmap.get(complement),i]
            
            hashmap[num] = i

        return []

        

            

        
        