class Solution:
    def silnia_i(self, n):
        s = 1
        for i in range(2, n+1):
            s *= i
        return s
        
    def uniquePaths(self, m: int, n: int) -> int:
        return int((self.silnia_i(m+n-2))/(self.silnia_i(m-1) * self.silnia_i(n-1)))
        