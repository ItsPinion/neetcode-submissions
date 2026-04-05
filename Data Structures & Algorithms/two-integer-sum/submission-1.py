class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for num in set(nums):
            complement = target - num
            if complement in set(nums):
                num_index = nums.index(num)
                complement_index = nums.index(complement, num_index + 1)
                if complement_index != -1:
                    return [num_index, complement_index]

        return []
