from itertools import product, permutations, combinations, combinations_with_replacement, groupby

prod = product([1, 2], [3, 4], [5, 6, 7])  # Retorna o produto cartesiano entre iteráveis
print('product', list(prod))

perm = permutations('abc', r=2)  # r é o comprimento desejado para as permutações (não obrigatório)
print('permutations', list(perm))  # Retorna todas as permutações possíveis de um iterável

comb = combinations('abc', 2)
print('combinations', list(comb))

cwr = combinations_with_replacement('abc', 2)
print('combinations with replacement', list(cwr))

gb = groupby('aaabbbccc')
for c, k in gb:
    print(c, list(k))
