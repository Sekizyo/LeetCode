class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for num in nums.copy():
            if num == val:
                k-=1
                nums.remove(val)