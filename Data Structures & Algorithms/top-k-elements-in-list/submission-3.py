class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1
        
        res = []

        for i in sorted(freqMap, key=lambda x: freqMap[x], reverse=True):
            if k == 0:
                break
            res.append(i)
            k -= 1
        
        return res


