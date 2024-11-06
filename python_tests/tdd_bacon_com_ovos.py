"""
1 - Recebe um número inteiro
2 - Saber se o número é multiplo de 3 e 5
    return bacon com ovos
3 - Saber se o número é multiplo somente de 3
    return bacon
4 - Saber se o número é multiplo somente de 5
    return ovos
5 - Saber se o número não é multiplo de 3 e 5
    return passa fome
"""


def bacon_com_ovos(x):
    assert isinstance((x), (int)), 'x deve ser int'
    if ((x % 3 == 0) and (x % 5 == 0)):
        return 'bacon com ovos'
    if (x % 3 == 0):
        return 'bacon'
    if (x % 5 == 0):
        return 'ovos'
    return 'passa fome'


print(bacon_com_ovos(15))
