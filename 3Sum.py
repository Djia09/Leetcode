nums = [-1, 0, 1, 2, -1, -4, 0, 0]
nums = [-1,0,1]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]

def sumNonZero(L, dic, solution):
    if len(L) < 2 or dic == {}:
        return solution
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            x = L[i] + L[j]
            if -x in dic:
                sol = sorted([L[i], L[j], -x])
                if sol not in solution:
                    solution.append(sol)
            return solution

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    solution = []
    Lzero = []
    Lpos = []
    Lneg = []
    dicPos = {}
    dicNeg = {}
    for x in nums:
        if x > 0:
            Lpos.append(x)
            dicPos[x] = x
        elif x < 0:
            Lneg.append(x)
            dicNeg[x] = x
        else:
            Lzero.append(x)
    if len(Lzero) >= 3:
        solution.append([0,0,0])

    if len(Lzero) >= 1:
        for i in range(len(nums)):
            x = nums[i]
            if x > 0:
                if -x in dicNeg:
                    sol = sorted([x, 0, -x])
                    if sol not in solution:
                        solution.append(sol)
            elif x < 0:
                if -x in dicPos:
                    sol = sorted([x, 0, -x])
                    if sol not in solution:
                        solution.append(sol)
    print("DEBUG: ", solution, Lpos, Lneg, dicPos, dicNeg)
    solution = sumNonZero(Lpos, dicNeg, solution)
    solution = sumNonZero(Lneg, dicPos, solution)
    
    return solution
solution = threeSum(nums)
print(solution)

class Solution:
  def sumNonZero(L, dic, solution):
    for i in range(len(L)):
      for j in range(i+1, len(L)):
        x = L[i] + L[j]
        print(x)
        if -x in dic:
          sol = [L[i], L[j], -x]
          if sol not in solution:
            solution.append(sol)
    return solution

  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    solution = []
    Lzero = []
    Lpos = []
    Lneg = []
    dicPos = {}
    dicNeg = {}
    for x in nums:
      if x > 0:
        Lpos.append(x)
        dicPos[x] = x
      elif x < 0:
        Lneg.append(x)
        dicNeg[x] = x
      else:
        Lzero.append(x)
    print(Lzero, Lpos, Lneg)
    if len(Lzero) >= 3:
      solution.append([0,0,0])

    if len(Lzero) >= 1:
      for i in range(len(nums)):
        x = nums[i]
        if x > 0:
          if -x in dicNeg:
            sol = list(set([x, 0, -x]))
            if sol not in solution:
              solution.append(sol)
        elif x < 0:
          if -x in dicPos:
            sol = list(set([x, 0, -x]))
            if sol not in solution:
              solution.append(list(set([x, 0, -x])))
    solution = sumNonZero(Lpos, dicNeg, solution)
    solution = sumNonZero(Lneg, dicPos, solution)
    
    return solution
        