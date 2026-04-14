class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        arr = [[v,k] for k, v in freq.items()]
        heapq.heapify_max(arr)
        res = []
        while k:
            res.append(heapq.heappop_max(arr)[1])
            k -= 1
        return res