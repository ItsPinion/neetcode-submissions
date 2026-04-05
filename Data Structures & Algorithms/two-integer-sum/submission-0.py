class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for num in set(nums):
            complement = target - num
            if complement in set(nums):
                return [nums.index(num), nums.index(complement, nums.index(num) + 1)]

        return []
