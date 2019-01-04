class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myhash = {}
        for i in range(len(nums)):
            myhash[nums[i]] = i
        for i in range(len(nums)):
            try:
                complement = target - nums[i]
                j = myhash[complement]
                if i != j:
                    return [i, j]
            except KeyError:
                pass;
        print("No solution !")
