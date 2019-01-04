x1 = 121
x2 = -121
x3 = 12
x4 = 1000030001

def isPalindrome(x):
  print('Input: ', x)
  L = list(str(x))
  n = len(L)
  if n == 1:
    return True
  elif n == 2:
    if L[0] == L[-1]:
      return True
    else:
      return False
  else:
    for i in range((n-1)//2+1):
      print(L[i], L[n-i-1])
      if L[i] != L[n-i-1]:
        return False
    return True

print(isPalindrome(x1))
print(isPalindrome(x2))
print(isPalindrome(x3))
print(isPalindrome(x4))