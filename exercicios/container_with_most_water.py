"""
Container with most water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

height = [1, 8, 6, 8, 4, 5, 3, 8]


def container(h):
    """
    Os números das extremidades devem ser analisados primeiramente. ile e ild representam índice lado esquerdo e índice
    lado direito respectivamente. A distância entre um e outro será multiplicada pelo menor valor entre estes e arma-
    zenada na lista res. Após a multiplicação os dois números são comparados, e se o da direita é maior o índice da
    esquerda é acrescido em +1, e se o número da esquerda é maior o índice da direita é decrescido em -1. Caso os dois
    sejam iguais o próximo valor da esquerda é comparado com o próximo valor da direita, e se na esquerda for encontrado
    um valor maior o índice da esquerda será acrescido em +1, e se o da direita for maior o índice da direita será
    decrescido em -1. Caso estes também sejam iguais não importa qual índice será alterado, portanto o da esquerda será
    o escolhido. Esse loop acontecerá enquanto índice da esquerda for menor que o da direita.

    :param h: Lista com valores a serem analisados a fim de encontrar o par que forma a maior área;
    :return: Maior área encontrada entre um par de valores da lista;
    """
    ile = 0
    ild = len(h) - 1
    res = []
    while ile < ild:
        res.append(min(h[ile], h[ild]) * (ild - ile))
        if h[ile] > h[ild]:
            ild -= 1
        elif h[ile] < h[ild]:
            ile += 1
        else:
            if h[ile + 1] > h[ild - 1]:
                ile += 1
            elif h[ile + 1] < h[ild - 1]:
                ild -= 1
            else:
                ile += 1
    return max(res)


print(container(height))
