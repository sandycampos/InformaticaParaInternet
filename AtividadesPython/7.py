turno = str(input('Informe o turno que você estuda: ')).upper().strip()[0]
if turno == 'M':
    print('Bom dia!')
elif turno == 'V' or turno == 'T':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido!')