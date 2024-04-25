class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count.keys():
                count[num] = 1
            else:
                count[num] += 1
        return min(count, key=count.get)
        