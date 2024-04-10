# Given a string s consisting of words and spaces, return the length of the last word in the string.

s = "luffy is still joyboy"
last = s.strip().split()[-1]
print(len(last))
