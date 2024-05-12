class Solution:
    def reverse(self, x: int) -> int:
        if len(str(x)) == 1:
            return x
        
        x = str(x)[::-1]

        if x[-1] == '-':
            x = x.replace('-', '')
            x = '-'+x
        
        if int(x) < -2**31 or int(x) > 2**31-1:
            return 0 
            
        if x[0] == '0':
            x = x.replace('0', '', 1)

        
        return int(x)

            

        
        