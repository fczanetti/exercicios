# Roman to Integer

# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

rom1 = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
rom2 = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}

n = 'LVIII'
res = []
while len(n) > 0:
    an = n[0:2] if len(n) >= 2 else n[0]
    if an in rom2:
        res.append(rom2[an])
    else:
        an = n[0]
        res.append(rom1[an])
    n = n.removeprefix(an)
print(sum(res))
