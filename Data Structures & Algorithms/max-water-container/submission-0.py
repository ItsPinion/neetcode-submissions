class Solution:
    def maxArea(self, heights: list[int]) -> int:
        f, b = 0, len(heights) - 1

        maximum_area: int = min(heights[f], heights[b]) * (b - f)

        while f < b:
            f += 1
            area = min(heights[f], heights[b]) * (b - f)
            if maximum_area < area:
                maximum_area: int = min(heights[f], heights[b]) * (b - f)

            b -= 1
            area = min(heights[f], heights[b]) * (b - f)
            if maximum_area < area and f < b:
                maximum_area: int = min(heights[f], heights[b]) * (b - f)

            pass

        return maximum_area
