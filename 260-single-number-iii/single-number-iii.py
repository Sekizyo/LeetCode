class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        numbers = {}
        for num in nums:
            if num not in numbers.keys():
                numbers[num] = 1
            else:
                numbers[num] += 1

        output = []
        for key, value in numbers.items():
            if value == 1:
                output.append(key)

        return output