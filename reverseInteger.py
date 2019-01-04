class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = 0
        L = str(x)
        if L[0] == '-':
            L = L[1:]
            neg += 1
        rev = 0
        dec = len(L) - 1
        for num in reversed(L):
            rev += int(num) * 10**dec
            dec-=1
        if neg > 0:
            rev = -rev
        
        if rev <= -(2**31) or rev >= (2**31) - 1:
            return 0
        return rev
