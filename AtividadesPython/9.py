tipo = int(input('Tipos de carne\n[0] Filé Duplo\n[1] Alcatra \n[2] Picanha \nEscolha: '))
quantidade = float(input('Quantidade em quilos: '))
forma = str(input('Pagamento com o cartão da loja? ')).upper().strip()[0]
carne = ('Filé Duplo','Alcatra','Picanha')

if quantidade < 5 and forma == 'N':
    if tipo == 0:
        total = quantidade * 4.9
    elif tipo == 1:
        total = quantidade * 5.9
    elif tipo == 2:
        total = quantidade * 6.9
    print('Informações da compra:',quantidade,'kg de',carne[tipo])
    print('Valor total: R$',round(total,2))

elif quantidade < 5 and forma == 'S':
    if tipo == 0:
        total = quantidade * 4.9
        desc = total * .05
        comDesc = total - desc
    elif tipo == 1:
        total = quantidade * 5.9
        desc = total * .05
        comDesc = total - desc
    elif tipo == 2:
        total = quantidade * 6.9
        desc = total * .05
        comDesc = total - desc
    print('Informações da compra:',quantidade,'kg de',carne[tipo])
    print('Valor total: R$',round(total,2))
    print('Deconto de R$',round(desc,2),'por utilizar o Cartão Tabajara')
    print('Valor a pagar: R$',round(comDesc,2))

elif quantidade > 5 and forma == 'N':
    if tipo == 0:
        total = quantidade * 5.8
    elif tipo == 1:
        total = quantidade * 6.8
    elif tipo == 2:
        total = quantidade * 7.8
    print('Informações da compra:',quantidade,'kg de',carne[tipo])
    print('Valor total: R$',round(total,2))

elif quantidade > 5 and forma == 'S':
    if tipo == 0:
        total = quantidade * 5.8
        desc = total * .05
        comDesc = total - desc
    elif tipo == 1:
        total = quantidade * 6.8
        desc = total * .05
        comDesc = total - desc
    elif tipo == 2:
        total = quantidade * 7.8
        desc = total * .05
        comDesc = total - desc
    print('Informações da compra:',quantidade,'kg de',carne[tipo])
    print('Valor total: R$',round(total,2))
    print('Deconto de R$',round(desc,2),'por utilizar o Cartão Tabajara')
    print('Valor a pagar: R$',round(comDesc,2))

else:
    print('Valores inválidos!')