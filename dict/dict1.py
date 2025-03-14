"""  Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela. """
# Pensando em como farei isso, 
# tenho como criar um input direto de um dicionario? a parte da media facil so preciso de um condicional 
#  no print eu crio um for k(modulo) , v(item) in aluno
aluno = dict()

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Media: '))
if aluno['media']<7:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'

for i , v in aluno.items():
    print(f'{i} é igual a {v}')
    


