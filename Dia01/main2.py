
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
  similaridade = 0
  for i in esquerda:
    similaridade += i * direita.count(i) 
  print(similaridade)
