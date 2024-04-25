class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)
        count = 0
        for nu in num[2:]:
            if nu == '1':
                count += 1

        return count
        