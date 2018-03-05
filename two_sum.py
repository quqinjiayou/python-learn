class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        for i in range(0, size):
            for j in range(i+1, size):
                if int(nums[i]) + int(nums[j]) == target :
                    res = [i, j]
                    return (i, j)

s = Solution()
x = str(raw_input("Please input the nums(seg by ,):"))
target = int(raw_input("Please input the target: "))
nums = x.split(",")

res = s.twoSum(nums, target)
print(res)