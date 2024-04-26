class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            for num2 in nums[i+1:]:
                if num + num2 == target:
                    return [i, nums.index(num2, i+1)]

        return []
