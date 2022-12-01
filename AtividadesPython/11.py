x = int(input('Insira um número para saber se ele é primo: '))

if x == 2 or x == 3 or x == 5 or x == 7:
    print(x, 'é um número primo!')
elif x == 1 or (x % 2 and x % 3 and x % 5 and x % 7) == 0:
    print(x,'não é um número primo!')
else:
    print(x, 'é um número primo!')