class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}

        # {
        #     4: 0,
        #     3: 1,
        #     ...
        #     ..
        #     .
        # }

        for i, num in enumerate(nums):
            compl = target - num

            if compl in numSet:
                return [numSet[compl], i]
            numSet[num] = i