"""  Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior. """

import random
from time import sleep
numeros = []

def sorteia():
    print('Sorteando valores da lista: ', end='')
    for _ in range(5):
        numeros.append(random.randint(0,100)) 
    for i in numeros:
        sleep(0.5)
        print(i,end=' ', flush=True)
    print()
    print('='*20)

def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma = soma + i
    print(soma)


sorteia()
somaPar(numeros)



