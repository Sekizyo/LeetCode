class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(len(nums[i:])):
                if abs(nums[i] - nums[i+j]) == k:
                    output += 1

        return output 
        