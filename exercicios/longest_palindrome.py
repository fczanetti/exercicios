# Given a string s, return the longest palindromic substring in s.

s = 'abcbabc'

itext = len(s) - 1  # Número de iterações externas
itint = itext  # Número de iterações internas que irá decrescer conforme iterações externas avançam
sil = rev = pl = ''  # Sílaba a ser analisada, reverso desta e palíndromo

for c in range(itext):
    fim = c + 2  # Limite da sílaba analisada
    for ch in range(itint):
        sil = s[c:fim]
        rev = sil[::-1]
        if sil == rev and len(sil) > len(pl):
            pl = sil
        fim += 1
    itint -= 1

print(pl)
