class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

#start test
s = Solution()
x = str(raw_input("Please input the nums(seg by ,):"))
target = int(raw_input("Please input the target: "))
nums = x.split(",")
nums =  [int(x) for x in nums]

res = s.twoSum(nums, target)
print(res)
