'''4. Faça um algoritmo que leia dois números reais e mostre o maior, o menor ou se
eles são iguais. '''


n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'O maior numero digitado foi:  {n1}e o menor foi {n2}')

elif n2 > n1:
    print(f' O maior numero digitado foi {n2} e o menor foi {n1}')

else:
    print('O numeros digitados são iguais ')