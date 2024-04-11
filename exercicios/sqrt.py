# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer
# should be non-negative as well.

def find_sqrt(x):
    left = 1
    mid, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid == x:
            break
        else:
            left = mid + 1
        if mid ** 2 < x < (mid + 1) ** 2:
            break
    return mid


print(find_sqrt(12))
