class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            current_area = (right - left) * min(height[left], height[right])
            # Update max_area if current_area is greater
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
