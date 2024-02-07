# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is
# closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

nums = [-1, 2, 1, -4]
target = 1

l = 0
menordist = dist = 0
nums.sort()
trio = []
while l < len(nums) - 2:
    m = l + 1
    r = len(nums) - 1
    while m < r:
        soma = nums[l] + nums[m] + nums[r]
        if soma > 0 > target or soma < 0 < target:
            dist = abs(abs(soma) + abs(target))
        elif soma > 0 and target > 0 or soma < 0 and target < 0:
            dist = abs(abs(soma) - abs(target))
        if menordist == 0:
            menordist = dist
            trio = [nums[l], nums[m], nums[r]]
        elif menordist > dist:
            menordist = dist
            trio = [nums[l], nums[m], nums[r]]
        if soma > target:
            r -= 1
        elif soma < target:
            m += 1
        else:
            break
        if m == r:
            l += 1
print(sum(trio))
print(trio)
