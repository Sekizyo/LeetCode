class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(sum(nums[:i+1]))

        return output