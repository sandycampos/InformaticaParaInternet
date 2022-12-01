pA = float(input('Valor do produto A: '))
pB = float(input('Valor do produto B: '))
pC = float(input('Valor do produto C: '))

if pA < (pB and pC):
    print('O produto A é mais barato! Compre por: R$',pA)
elif pB < (pB and pC):
    print('O produto B é mais barato! Compre por: R$',pB)
else:
    print('O produto C é mais barato! Compre por: R$',pC)