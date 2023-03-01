print('='*40)
print(' 10 TERMOS DE UMA PROGRESSÃO ARITIMÉTICA')
print('='*40)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont += 1
print('FIM',end='')