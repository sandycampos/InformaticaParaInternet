n1 = int(input('Insira um valor: '))
n2 = int(input('Insira um valor: '))
n3 = int(input('Insira um valor: '))

if n1 > (n2 and n3):
    print('O número',n1,'é maior.')
elif n2 > (n1 and n3):
    print('O número',n2,'é maior.')
else:
    print('O número',n3,'é maior.')
    