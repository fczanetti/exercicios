# Given a string s, find the length of the longest substring without repeating characters.

s = "abcabcdbb"
ls = []
big = []
for i, c in enumerate(s):
    for ch in s[i:]:
        if ch not in ls:
            ls.append(ch)
        else:
            if len(ls) > len(big):
                big = ls
                ls = []
                break
            else:
                ls = []
                break
print(len(big))
