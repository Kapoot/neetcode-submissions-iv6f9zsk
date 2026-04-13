class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        myset = set()

        for num in nums:
            if num not in myset:
                myset.add(num)
            else:
                return True
        
        return False
         