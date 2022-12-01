peso = int(input('Insira o peso em quilos: '))
excesso = (peso - 50)
multa = (excesso * 4)

if peso > 50:
    print('Sua pesca excedeu',excesso,'kg. Multa:',multa,'R$.')
else:
    print('Você não precisa pagar multa!')