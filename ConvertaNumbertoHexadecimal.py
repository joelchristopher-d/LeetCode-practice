class Solution:
    def toHex(self, num: int) -> str:
        if num==0:return '0'
        hex_digits = '0123456789abcdef'
        num= (1 << 32) + num if num<0 else num
        hexa=""
        while num:
            hexa=hex_digits[num%16]+hexa
            num//=16
        return hexa
                
