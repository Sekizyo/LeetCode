class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        for _ in range(count):
            nums.remove(0)
        
        for _ in range(count):
            nums.append(0)
        