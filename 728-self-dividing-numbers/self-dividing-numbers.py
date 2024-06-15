class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for number in range(left, right+1):  
            splitted = str(number)

            if '0' in splitted:
                continue
            
            for num in splitted:
                if number % int(num) != 0:
                    break    
            else:
                output.append(number)

        return output