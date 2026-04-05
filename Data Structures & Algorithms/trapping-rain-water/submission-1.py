class Solution:
    def trap(self, height: list[int]) -> int:

        
        l = 0
        r = len(height) - 1

        max_l = height[l]
        max_r = height[r]

        ans = 0
        while l < r:

            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                ans += max(max_l - height[l], 0)
            else:
                r -= 1
                max_r = max(max_r, height[r])

                ans += max(max_r - height[r], 0)
        
        return ans
