print('*' * 30)
print('{:^30}'.format('BANCO DENN'))
print('*' * 30)
valor = int(input('Digite o valor que deseja sacar R$: '))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cedulas de ${ced:.2f} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        if total == 0:
            break
        totCed=0
print('-='*20)