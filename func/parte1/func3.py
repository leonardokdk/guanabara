""" Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada """
from time import sleep
def contador(entrada, saida , passo):
    print('-'*20)
    print(f'Contador de {entrada} até {saida}')
    for i in range(entrada, saida, passo):
        print(i, end=' ', flush = True)
        sleep(0.5)
    print()

contador(1,10,1)
contador(10,-1,-1)
print('AGORA É SUA VEZ!!')
contador(int(input('Entrada: ')), int(input('Até: ')), int(input('Passo: ')) )