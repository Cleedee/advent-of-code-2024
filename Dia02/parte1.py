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

def estah_ordenado(niveis):
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

def tem_entre_um_e_tres():
    pass

def eh_seguro(relatorio: str) -> bool:
    niveis = [int(nivel) for nivel in relatorio.split()]
    if not estah_ordenado(niveis):
        return False
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

linhas = dados.split('\n')
linhas = list(filter(None, linhas))

seguros = 0

for linha in linhas:
    seguros += 1 if eh_seguro(linha) else 0

assert eh_seguro("7 6 4 2 1") == True
assert eh_seguro("1 3 6 7 9") == True
assert eh_seguro("9 7 6 2 1") == False
assert seguros == 2

with open('./entrada.txt') as file:
    linhas = file.readlines()
    relatorios = list(filter(None, linhas))
    seguros = 0
    for relatorio in relatorios:
        seguros += 1 if eh_seguro(relatorio) else 0

print(seguros)
