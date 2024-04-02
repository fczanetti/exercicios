# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No
# two characters may map to the same character, but a character may map to itself.

s = 'title'
t = 'paper'


def isomorphic(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    pair = {}
    for i, c in enumerate(s1):
        cs2 = s2[i]
        if c in pair and cs2 != pair[c]:
            return False
        pair[c] = s2[i]
    return True


print(isomorphic(s, t))
