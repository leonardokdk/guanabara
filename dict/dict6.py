""" Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
 visualização de detalhes do aproveitamento de cada jogador. """

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
jogadores = list()
total = 0
gols = dict()


while True:
    gols['nome'] = input('Nome do jogador: ')
    partidas = int(input(f"Quantas partidas {gols['nome']} jogou? "))
    gols["gols"] = [int(input(f'Quantos gols na partida {i}: ')) for i in range(partidas)]
    for i in range(partidas):
        total += gols['gols'][i]
    gols['total'] = total
    jogadores.append(gols.copy())
    escolha = input('Quer continuar? [S/N]').upper()
    if escolha != 'S':
        break

for i in range(jogadores.__len__()):
    print(f"{i} {jogadores[i]['nome']} {jogadores[i]['gols']} {jogadores[i]['total']}")

print('=-=-'*10)

while True:
    escolha = int(input('Mostrar dados de qual jogador? 999 para parar '))
    if escolha == 999:
        break
    jogador = jogadores[escolha]
    for i in range(jogador['gols'].__len__()):
        print(f"No jogo {i} fez {jogador['gols'][i]} gols")
    










""" for i , v in gols.items():
    print(f'O campo {i} tem o valor {v}')


print('=-'*10)
print(f"O jogador {gols['nome']}")
for i in range(0,partidas):
    print(f'Na partida {i}, fez {gols["gols"][i]} gols')
print(f'Foi um total de {total} gols.') """
