class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum = 0 
        rightSum = 0

        for pivot in range(len(nums)):
            a = nums[0:pivot]
            b = nums[pivot+1:]
            leftSum = sum(a)
            rightSum = sum(b)
            if leftSum == rightSum:
                return pivot

        return -1