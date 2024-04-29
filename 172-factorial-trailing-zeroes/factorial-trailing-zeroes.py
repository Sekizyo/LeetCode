import sys
sys.set_int_max_str_digits(0)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        m = 1
        for i in range(1, n+1):
            m *= i

        count = 0
        mList = str(m)

        for i in range(len(mList)-1, 0, -1):
            if mList[i] == '0':
                count += 1
            else:
                break
        
        return count