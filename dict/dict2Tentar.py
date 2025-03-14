"""  Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado. """

# vamos quebrar o problema
# Primeiro preciso que 4 jogadores joguem um dado, vou colocar um input com o nome dos jogadores que vão
# ser armazenados em dicionarios dentro de uma lista
# os 'dados' serão um random.radint(range 1,7)
# ao final pra verificar quem é o vencedor vou percorrer a lsita com um for, e dentro desse 
# for vou criar outro for pra percorrer as notas 
# ou posso usar um sort, talvez funcione
# e se der empate??  colocar como primeiro quem jogou o dado primeiro 
# Entao preciso armazenar tambem o numero do jogador
import random

players = []
jogador = dict()

for i in range(0,2):
    jogador['nome'] = input('Nome do jogador')
    jogador['dado'] = random.randint(1,7)
    players.append(jogador.copy())

print(players)
    