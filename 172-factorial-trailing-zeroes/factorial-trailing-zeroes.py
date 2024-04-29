import sys
import math
sys.set_int_max_str_digits(0)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        m = math.factorial(n)
        count = 0
        mList = list('%d' % m)

        for i in range(len(mList)-1, 0, -1):
            char = mList[i]
            if char == '0':
                count += 1
            else:
                break
        
        return count