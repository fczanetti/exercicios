# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

nums = [-1, 0, 1, 2, -1, -4, 2, 2, 1, 1, -1, -4, -4]
nums.sort()
i = 0
res = []
while i <= len(nums) - 3:
    j = i + 1
    k = len(nums) - 1
    while j < k:
        psom = nums[i] + nums[j] + nums[k]
        if psom < 0:
            j += 1
            while nums[j] == nums[j - 1]:
                j += 1
        if psom > 0:
            k -= 1
            while nums[k] == nums[k + 1]:
                k -= 1
        if psom == 0:
            res.append([nums[i], nums[j], nums[k]])
            j += 1
            while nums[j] == nums[j - 1] and j < k:  # teste
                j += 1  # teste
            k -= 1
            while nums[k] == nums[k + 1] and k > j:  # teste
                k -= 1  # teste
        if j >= k:
            i += 1
            while nums[i] == nums[i - 1] and i < j:
                i += 1
print(res)
