class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in my_set:
                continue
            else:
                count = 1
                while (num + count) in my_set:
                    count += 1
                longest = max(longest, count)
        
        return longest
            




        