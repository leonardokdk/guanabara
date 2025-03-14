"""  Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média """

""" Vou precisar guardar em um dicionario nome, sexo, idade de varias pessoas
cada pessoa vai estar dentro de uma lista vou precisar deixar isso em um while == true e um condicional
que da break
    pra verificar quantas pessoas foram cadastradas posso dar um len na lista
    a media das idades eu posso conseguir com um for que percorre cada indice da lista, dentro de outro for
que percorre todas as idades que sao somadas a uma variavel chamada total, e divididas pelo len da lista
    Criar uma lista so com os indices da lista que tem como valor do sexo feminino
    criar um condicional que pega o valor da media de idade, e verifica quem está acima e adiciona em uma 
lista chamada acimaMedia
 """
individuo = dict()
pessoas = list()
mulheres = list()
acimaDaMedia = list()
escolha = str
total = 0

while True:
    print('=-=-=-'*10)
    individuo['nome'] = input('Digite seu nome: ')
    individuo['sexo'] = input('Qual seu sexo:F/M ').upper()
    individuo['idade'] = int(input('Qual sua idade: '))
    pessoas.append(individuo.copy())
    print('=*'*10)
    escolha = input('Digite N para sair ou qualquer tecla pra continuar. ').upper()
    if escolha == 'N':
        break

# Quantas pessoas tem cadastradas
print('=-=-=-'*10)
print(f'Pessoas cadastradas: {pessoas.__len__()}')

# calculo de media
for i in range(pessoas.__len__()):
    total += pessoas[i]['idade']
media = total/pessoas.__len__()

# Coloca as mulheres dentro de uma lista separada
for i in range(pessoas.__len__()):
    if pessoas[i]['sexo'] == 'F':
        mulheres.append(pessoas[i])

#Separa quem está acima da media em uma lista
for i in range(pessoas.__len__()):
    if pessoas[i]['idade'] > media:
        acimaDaMedia.append(pessoas[i])


print(f'Media de idade: {media}')
print(mulheres)
print(acimaDaMedia)