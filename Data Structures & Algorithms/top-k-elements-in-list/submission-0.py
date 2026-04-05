class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency: dict[int, int] = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        print(frequency)

        return sorted(frequency, key=frequency.get, reverse=True)[:k]