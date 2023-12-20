# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
# signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

n = -321


def invert(v):
    if v > (2**31 - 1) or v < -2**31:
        return 0
    else:
        s = str(v)
        aux = []
        for ch in s[::-1]:
            if ch == '-':
                aux.insert(0, ch)
            else:
                aux.append(ch)
        return int(''.join(aux))


print(invert(n))
