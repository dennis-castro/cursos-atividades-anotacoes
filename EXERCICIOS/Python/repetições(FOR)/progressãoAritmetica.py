print('='*20)
print(' 10 TERMOS DE UMA PROGRESSÃO ARITIMÉTICA')
print('='*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('razão: '))
decimo = primeiro + (11-1) * razao

for c in range (primeiro, decimo, razao):
    print('{}'.format(c),end=' -> ')
print('ACABOU')