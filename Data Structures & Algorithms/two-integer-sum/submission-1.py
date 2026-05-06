class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in my_dict:
                return [my_dict[complement], i]
            my_dict[num] = i
        
        return []
        