class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        res = int(''.join(s)) + 1
        output = [int(x) for x in str(res)]

        return output
        