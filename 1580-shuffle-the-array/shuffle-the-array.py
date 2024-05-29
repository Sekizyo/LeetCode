class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        x = nums[0:n]
        y = nums[n:]
        for i in range(n):
            output.append(x[i])
            output.append(y[i])
        return output
        