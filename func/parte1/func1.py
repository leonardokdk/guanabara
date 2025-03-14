def area():
    print('Controle de terrenos')
    print('-'*30)

    a = float(input('Largura (m): '))
    b = float(input('Comprimento (m): '))
    area = a * b
    print(f'A area de um terreno {a}x{b} é de {area}m²')

area()