area = int(input('Informe o tamanho em m²: '))

if area % 54 == 0:
    lata = int(area / 54)
    valor = (lata * 80)
    print('Você precisa de',lata,'lata(s) de tinta. Valor total: R$',valor)
else:
    lata = int(area / 54) + 1
    valor = (lata * 80)
    print('Você precisa de',lata,'latas(s). Valor total: R$',valor)