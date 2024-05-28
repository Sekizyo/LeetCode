class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum0 = 0
        for num in nums:
            if nums.count(num) == 1:
                sum0 += num

        return sum0
        