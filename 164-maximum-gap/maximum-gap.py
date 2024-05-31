class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maxGap = 0
        for i in range(0, len(nums)-1):
            diff = nums[i+1]-nums[i]
            if diff > maxGap:
                maxGap = diff

        return maxGap
        