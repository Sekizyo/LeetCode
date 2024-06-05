class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []

        for num in nums:
            splitted = list(str(num))
            for n in splitted:
                output.append(int(n))
        
        return output