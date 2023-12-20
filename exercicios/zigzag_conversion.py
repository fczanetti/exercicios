"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

"""

s = 'PAYPALISHIRING'

linha = 1  # Linha que será acrescida do valor adc para auxiliar na inclusão das letras no dicionário;
adc = 0
numlinhas = 3  # Número de linhas desejado para a resposta;
dct_linhas = {n: [] for n in range(1, (numlinhas + 1))}  # Dicionário que agrupará cada letra em sua posição(linha);

for ch in s:
    dct_linhas[linha].append(ch)
    if linha == 1:
        adc = 1
    if linha == numlinhas:
        adc = -1
    linha += adc

res = []
for linha in dct_linhas.values():
    res.extend(linha)
print(f'Resultado: {"".join(res)}')
