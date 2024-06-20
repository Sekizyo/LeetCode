class Solution(object):
    def firstMissingPositive(self, nums):
        nums.sort()
        i = 1
        for j in nums:
            if j == i:
                i+=1
        return i