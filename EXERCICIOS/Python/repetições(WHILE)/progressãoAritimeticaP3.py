print('='*40)
print(' 10 TERMOS DE UMA PROGRESSÃO ARITIMÉTICA')
print('='*40)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM...total de termos  {} exibidos '.format(total))