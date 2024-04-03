# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


s_dict = {'(': ')', '{': '}', '[': ']'}
st = '(}'


def valid_parentheses(s: str):
    if len(s) % 2 != 0:
        return False
    for i in range(0, len(s), 2):
        if s[i+1] != s_dict[s[i]]:
            return False
    return True


print(valid_parentheses(st))
