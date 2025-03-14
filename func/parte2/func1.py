""" Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de 
nascimentode uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
OPCIONAL e OBRIGATÓRIO nas eleições. """

def voto(anoDeNascimento):
    idade = 2025 - anoDeNascimento 
    if idade >= 65:
        voto = 'Voto Opcional'
    elif idade >= 18 and idade < 65:
        voto= 'Voto Obrigatorio'
    elif idade >= 16:
        voto = 'Voto opcional'
    else:
        voto = 'Não pode votar'
    
    return voto


resultado = voto(2010)
print(resultado)