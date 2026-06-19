class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for i, num in enumerate(nums):
            compl = target - num

            if compl in seenMap:
                return [seenMap[compl], i]
            seenMap[num] = i