""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. """


"""Então preciso de um dicionario com nome, nascimento, ctps 
se a pessoa não tiver ctps ela digita 0
ano de contratação e salario
calcular a idade e quantos anos a pessoa vai se aposentar
são 35 anos de trabalho pra alguem se aposentar
"""

individuo = dict()
individuo['nome'] = input('Digite seu nome: ')
individuo['nascimento'] = int(input('Ano de nascimento: '))

ctps = int(input('Numero da ctps: (Digite 0 se não tiver) '))
if ctps != 0:
    individuo['ctps'] = ctps
    
individuo['contratacao'] = int(input('Ano de contração: '))
individuo['salario'] = float(input('Digite seu salario: '))

individuo['idade'] =  2025 - individuo['nascimento'] 

individuo['aposento'] = individuo['idade'] + (35 - (2025- individuo['contratacao'] ))

for i , k in individuo.items():
    print(i , k)