import time

def maior(*num):
    maiorNumero = 0
    print('-='*20)
    print('Analisando os valores passados...')
    print(f"{num} foram informados {num.__len__()} valores ao todo")
    for i in num:
        if i > maiorNumero:
            maiorNumero=i
    print(f'O maior valor informado foi {maiorNumero}.')


maior(1,7,2,7,3,2,1,10)