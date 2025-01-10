
with open('./entrada.txt') as file:
  linhas = file.readlines()
  linhas = [linha.split() for linha in linhas if linha != '\n']
  esquerda = []
  direita = []
  for linha in linhas:
    esquerda.append(int(linha[0]))
    direita.append(int(linha[1]))
  esquerda.sort()
  direita.sort()
  total = 0
  for i in range(len(esquerda)):
    total += abs(esquerda[i] - direita[i])
  print(total)
