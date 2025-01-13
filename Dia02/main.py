# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

dados = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def tem_nivel_repetido(relatorio:str) -> bool:
    niveis = [int(nivel) for nivel in relatorio.split()]
    conjunto = set(niveis)
    return len(niveis) != len(conjunto))

def primeiro_repetido(relatorio: str) -> int:
    niveis = [int(nivel) for nivel in relatorio.split()]
    vistos = set()
    for nivel in niveis:
        if nivel in vistos:
            return nivel
        vistos.add(nivel)

def estah_ordenado(relatorio):
    niveis = [int(nivel) for nivel in relatorio.split()]
    if niveis[0] > niveis [-1]:
        # relatorio provavelmente decrescente
        ordenado = niveis[:]
        ordenado.sort(reverse=True)
        if ordenado == niveis:
            return True
    elif niveis[0] < niveis[-1]:
        # relatorio provavelmente crescente
        ordenado = niveis[:]
        ordenado.sort()
        if ordenado == niveis:
            return True
    return False


def eh_seguro(relatorio: str) -> bool:
    niveis = [int(nivel) for nivel in relatorio.split()]
    # verificar diferenca entre os elementos
    # não pode ser igual ou maior que quatro (4)
    atual = 0
    for i in range(len(niveis)):
        # 1 3 5 6 8 10
        # 0 1 2 3 4 5
        # tamanho = 6
        # indice = 5
        if i + 1 == len(niveis):
            return True
        atual = niveis[i]
        posterior = niveis[i+1]
        if not abs(atual - posterior) in (1,2,3):
            return False
    return False

assert eh_seguro('1 2 8 9') == False
assert eh_seguro("7 6 4 2 1") == True
assert eh_seguro("1 3 6 7 9") == True
assert eh_seguro("9 7 6 2 1") == False

def separar_em_pares(lista):
    pares = []
    for i in range(len(lista) - 1):
        par = (lista[i], lista[i+1])
        pares.append(par)
    return pares

def problema_dampener(relatorio: str) -> str:
    return relatorio

assert problema_dampener('7 6 4 2 1') == '7 6 4 2 1'
assert problema_dampener('1 2 7 8 9') == '1 2 8 9'
assert eh_seguro('1 2 8 9') == False
assert problema_dampener('9 7 6 2 1') == '9 7 6 1'
assert eh_seguro('9 7 6 1') == False
assert problema_dampener('1 3 2 4 5') == '1 2 4 5'
assert eh_seguro('1 2 4 5') == True

linhas = dados.split('\n')
linhas = list(filter(None, linhas))

seguros = 0

for linha in linhas:
    if estah_ordenado(linha):
        seguros += 1 if eh_seguro(linha) else 0

assert seguros == 2


with open('./entrada.txt') as file:
    linhas = file.readlines()
    relatorios = list(filter(None, linhas))
    seguros = 0
    relatorios_inseguros = []
    for relatorio in relatorios:
        if not eh_seguro(relatorio):
            relatorios_inseguros.append(relatorio)
        else:
            seguros += 1

print('Parte 1: ', seguros)
