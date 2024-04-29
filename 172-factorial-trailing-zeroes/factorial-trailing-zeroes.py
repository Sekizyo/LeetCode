import sys
import math
sys.set_int_max_str_digits(0)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        m = str(math.factorial(n))

        for i in range(len(m)-1, 0, -1):
            if m[i] == '0':
                count += 1
            else:
                break
        
        return count