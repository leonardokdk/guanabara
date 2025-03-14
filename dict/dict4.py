""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
 """
""" 
O programa vai ler o nome
do jogador e quantas partidas ele jogou
um input de variavel nome e outra que recebe a quantidade de jogos
essa variavel vai em um for range(0, count)
dentro desse for vou colocar o dicionario
o dicionario recebe a partida(i) e a quantidade de gols, que e guardado em uma lista
 """
total = 0
gols = dict()
gols['nome'] = input('Nome do jogador: ')
partidas = int(input(f"Quantas partidas {gols['nome']} jogou? "))

gols["gols"] = [int(input(f'Quantos gols na partida {i}: ')) for i in range(partidas)]

print('=-'*10)

for i in range(partidas):
    total += gols['gols'][i]
gols['total'] = total
print(gols)
print('=-'*10)

for i , v in gols.items():
    print(f'O campo {i} tem o valor {v}')


print('=-'*10)
print(f"O jogador {gols['nome']}")
for i in range(0,partidas):
    print(f'Na partida {i}, fez {gols["gols"][i]} gols')
print(f'Foi um total de {total} gols.')
