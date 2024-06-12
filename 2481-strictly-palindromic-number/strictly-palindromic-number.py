import numpy
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n-1):
            nr = numpy.base_repr(n, base=base)
            if nr != nr[::-1]:
                return False
        return True