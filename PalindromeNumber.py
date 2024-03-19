class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        y=x
        z=0
        while y:
            z=(z*10)+y%10
            y//=10
        return x==z

        
