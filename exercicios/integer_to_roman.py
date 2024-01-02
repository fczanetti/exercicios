# Given an integer, convert it to a roman numeral.

algs = {1000: 'M', 900: 'CM', 500: 'D',
        400: 'CD', 100: 'C', 90: 'XC',
        50: 'L', 40: 'XL', 10: 'X',
        9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
num = 1994
r = ''

for n in algs:
    if n > num:
        continue
    res = num // n
    if res == 1:
        r += algs[n]
        num -= res * n
    elif res > 1:
        if (res * n) in algs:
            r += algs[res * n]
        else:
            r += (algs[n] * res)
        num -= res * n
    if num == 0:
        break
print(r)
