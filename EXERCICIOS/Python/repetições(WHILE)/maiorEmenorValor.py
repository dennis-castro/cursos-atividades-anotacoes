resp = 'S'
media = maior = menor = cont = soma = 0

while resp in 'Ss':
    num = int(input('Digite um numero: '))
    resp = str(input('Voce deseja continuar? [S/N]: ')).strip().upper()[0]
    cont += 1
    soma += num
    if cont == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('Você digitou {} numeros e a media deles é {:.2f}'.format(cont, media))
print('A soma entre os valores foi {}, e o maior numero foi {}, e o menor {}.'.format(soma, maior, menor))
print('fim')