class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        output = 0
        for i, num1 in enumerate(nums):
            for num2 in nums[i+1:]:
                if num1 + num2 < target:
                    output += 1

        return output
        