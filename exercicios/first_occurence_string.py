# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.


haystack = "tfsadghhsad"
needle = "sad"
ln = len(needle)


def find_needle(n: str, h: str):
    if n not in h:
        return -1
    else:
        c = 0
        while c <= len(haystack) - len(needle):
            if haystack[c] != needle[0]:
                c += 1
                continue
            possib_needle = haystack[c:c + len(needle)]
            if possib_needle == needle:
                return c
            else:
                c += 1
        # return h.find(n)


if __name__ == '__main__':
    print(find_needle(needle, haystack))
