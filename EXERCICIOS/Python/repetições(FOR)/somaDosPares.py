somaPar = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} numero: '.format(c)))
    if num % 2 == 0:
        somaPar = somaPar + num
        cont = cont + 1

print('\033[31mVoce informou {} numeros PARES e a soma deles SÃO: {}\033[m'.format(cont, somaPar))