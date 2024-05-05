class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(0, n+1):
            b = bin(i)
            output.append(str(b).count('1'))

        return output