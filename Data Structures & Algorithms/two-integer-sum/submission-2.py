class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for num in set(nums):
            complement = target - num
            if complement in set(nums):
                num_index = nums.index(num)
                if complement == num:
                    complement_index = nums.index(complement, num_index + 1)
                else:
                    complement_index = nums.index(complement)
                return [num_index, complement_index]

        return []

