class Solution:
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        digits = list("0123456789")
        if string.strip() == "":
            return 0
        charac = string.strip().split(' ')[0]
        charac = charac.split('.')[0]
        neg = 0
        if charac == "":
            return 0
        try:
            if charac[0] == '+':
                if charac[1] != '-' and charac[1] != '+':
                    charac = charac[1:]
                else:
                    return 0
            if charac[0] == '-':
                neg += 1
                print(int(charac[1]))
                charac = charac[1:]
                num = -int(charac)
            else:
                num = int(charac)
        except ValueError:
            num = 0
            k = 0
            print('Hello: ', charac, neg)
            while True:
                try:
                    if charac[k] not in digits:
                        break;
                    else:
                        if neg > 0:
                            num = -int(charac[:k+1])
                        else:
                            num = int(charac[:k+1])
                        k += 1
                except IndexError:
                    break;
        except IndexError:
            return 0
        if num >= 2**31-1:
            return 2**31-1
        elif num < -(2**31):
            return -(2**31)
        return num
