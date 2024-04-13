# You are given an integer N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art
# based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:

# size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

n = 5
a = 'abcdefghijklmnopqrstuvwxyz'
txt = a[:n]
c1 = -1
s = ''
spaces = 4 * n - 3
for i in range(0, 2 * n - 1):
    s += txt[-1:c1:-1]
    s += txt[c1:]
    if len(s) > 1:
        s = list(s)
    print('-'.join(s).center(spaces, '-'))
    s = ''
    if i < n - 1:
        c1 -= 1
    else:
        c1 += 1
