class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return 2 indices (who add up to target)

        seen = {}
        
        for i, num in enumerate(nums):
            compl = target - num

            if compl in seen:
                return [seen[compl], i]

            seen[num] = i