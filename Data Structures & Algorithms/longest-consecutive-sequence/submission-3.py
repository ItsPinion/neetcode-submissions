class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        if not len(nums):
            return 0
            
        nums_set = set(nums)

        longest = 1

        for num in nums_set:
            if num - 1 in nums_set:
                i = num
                count = 1
                while i in nums_set:
                    count += 1

                    i += 1

                if longest < count:
                    longest = count

        return longest

