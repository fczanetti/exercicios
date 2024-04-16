# Write a recursive algorithm to find the min and max value from a list of integers.

ls = [1, 5, 2, 4, 9, 7, 0, 12]


def _min_max(l, c, mini, maxi):
    if mini == 0 and maxi == 0:
        mini, maxi = l[c], l[c]
    else:
        if l[c] > maxi:
            maxi = l[c]
        if l[c] < mini:
            mini = l[c]
    c += 1
    if c < len(l):
        return _min_max(l, c, mini, maxi)
    else:
        return mini, maxi


def min_max(l: list):
    return _min_max(l, c=0, mini=0, maxi=0)


if __name__ == '__main__':
    print(min_max(ls))
