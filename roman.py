class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 50, "XC": 90, "CD": 400, "CM": 900}
        special = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        num = 0
        i = 0
        while i < len(s):
            try:
                num += special[s[i:i+2]]
                i += 2
            except KeyError:
                num += dic[s[i]]
                i += 1
        return num
