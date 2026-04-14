class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        curr = 0
        right = len(nums) - 1

        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1        # safe to advance, left side is already sorted
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
                # do NOT advance curr - the swapped value is unknown
            else:
                curr += 1        # it's a 1, just move on

            
            

            
            
                
        