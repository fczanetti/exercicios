# HackerRank - Maximize It

# You are given a function f(x) = x**2. You are also given K lists. The i(th) list consists of Ni elements.
# You have to pick one element from each list so that the value from the equation below is maximized:
#
# S = (f(X1) + f(X2) + ... + f(Xk)) % M
#
# Xi denotes the element picked from the i(th) list. Find the maximized value Smax obtained.
# % denotes the modulo operator.
# Note that you need to take exactly one element from each list, not necessarily the largest element. You add the
# squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the
# answer to the problem.
# Input Format:
# The first line contains 2 space separated integers K and M.
# The next K lines each contains an integer Ni, denoting the number of elements in the i(th) list, followed by Ni
# space separated integers denoting the elements in the list.

from itertools import product

K, M = tuple(map(int, input().split()))
ls = []
for _ in range(K):
    Ni = list(map(int, input().split()))
    i = Ni.pop(0)
    ls.append(Ni)

s = 0
maior = 0
for c in list(product(*ls)):
    for v in c:
        s += v ** 2
    vf = s % M
    if maior < vf:
        maior = vf
    s = 0
print(maior)
