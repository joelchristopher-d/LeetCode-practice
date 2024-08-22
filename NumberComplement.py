class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return "1"
    
        binary = ""
        while num > 0:
            remainder = num % 2
            temp = "0" if remainder==1 else "1"
            binary = temp + binary
            num = num // 2
        decimal = 0
        for digit in binary:
            decimal = decimal*2 + int(digit)
        return decimal
        
