class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            if len(str(num)) % 2 == 0:
                num = str(num)

                left  = list(num[:len(num)//2])
                right = list(num[len(num)//2:])

                leftF = []
                rightF = []
                for num1 in left:
                    leftF.append(int(num1))
                
                for num2 in right:
                    rightF.append(int(num2))

                if sum(leftF) == sum(rightF):
                    count += 1

        return count
