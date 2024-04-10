# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
# integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
# does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

digits = [1, 3, 9, 9]


def sum_one(ls: list):
    c = 0
    for d in ls[::-1]:
        c += 1
        if d == 9:
            ls[-c] = 0
        else:
            ls[-c] += 1
            return ls
    return [1] + ls


if __name__ == '__main__':
    print(sum_one(digits))
