def twoSum(nums, target):
        nums_bak = nums.copy()
        nums.sort()
        i = 0
        j = 0
        for k in range(0, (len(nums) - 1)):
            if nums[k] + nums[k + 1] >= target:
                i = k
                j = k + 1
                break
        while i >= 0 and j < len(nums):
            if nums[i] + nums[j] < target:
                j += 1
            elif nums[i] + nums[j] > target:
                i -= 1
            else:
                if nums[i] == nums[j]:
                    return [nums_bak.index(nums[i]), nums_bak.index(nums[j], i + 1)]
                else:
                    return [nums_bak.index(nums[i]), nums_bak.index(nums[j])]

print(twoSum([2,4,6,1,3,5,7],7))