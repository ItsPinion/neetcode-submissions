class Solution:
    def maxArea(self, heights: list[int]) -> int:
        f, b = 0, len(heights) - 1

        maximum_area: int = min(heights[f], heights[b]) * (b - f)

        while f < b:
            if heights[f] > heights[b]:
                b -= 1
            else:
                f += 1
            area = min(heights[f], heights[b]) * (b - f)
            if maximum_area < area:
                maximum_area: int = area

        return maximum_area
