# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

nums = [-2, 1, 2, 4, 5, 6, 7, 9, 11, 12, 15, 18, 27]
target = 10


def find_insert_position(n: list, t: int):
    if t in n:
        return f'Índice: {n.index(t)}'
    elif t > n[-1]:
        return f'Índice: {len(n)}'
    elif t < n[0]:
        return 'Índice: 0'
    else:
        left = 0
        right = len(nums) - 1
        mid = len(nums) // 2
        while True:
            if target > n[mid]:
                if target <= n[mid + 1]:
                    return f'Índice: {mid + 1}'
                left = mid
                mid = (right - left) // 2 + left
            elif target < n[mid]:
                if target >= n[mid - 1]:
                    return f'Índice: {mid}'
                right = mid
                mid = (right - left) // 2 + left


if __name__ == '__main__':
    print(find_insert_position(nums, target))
