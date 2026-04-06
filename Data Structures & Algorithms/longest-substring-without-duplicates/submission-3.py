class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        front = 0
        current: set[str] = set()

        longest = 0

        for c in s:
            while c in current:
                current.remove(s[front])
                front += 1

            current.add(c)
            longest = max(longest, len(current))

        return longest
